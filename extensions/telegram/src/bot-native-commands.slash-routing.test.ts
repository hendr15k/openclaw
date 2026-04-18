import { describe, expect, it } from "vitest";
import {
  buildTelegramNativeCommandCallbackData,
  parseTelegramNativeCommandCallbackData,
} from "./bot-native-commands.js";

/**
 * Unit tests for the telegram slash text routing functions.
 * These functions support routing of slash commands entered as text (not via /)
 * through native command handlers.
 *
 * Related: commit b2b76065 ("fix: route telegram slash text through native handlers")
 */
describe("Telegram slash text routing functions", () => {
  // -------------------------------------------------------------------------
  // buildTelegramNativeCommandCallbackData
  // -------------------------------------------------------------------------

  describe("buildTelegramNativeCommandCallbackData", () => {
    it("prefixes a slash command with tgcmd:", () => {
      expect(buildTelegramNativeCommandCallbackData("/help")).toBe("tgcmd:/help");
    });

    it("prefixes a plain command name with tgcmd:", () => {
      expect(buildTelegramNativeCommandCallbackData("status")).toBe("tgcmd:status");
    });

    it("preserves full command text including arguments", () => {
      expect(buildTelegramNativeCommandCallbackData("/model claude")).toBe("tgcmd:/model claude");
    });

    it("handles command with hyphenated name", () => {
      expect(buildTelegramNativeCommandCallbackData("/export-session")).toBe(
        "tgcmd:/export-session",
      );
    });

    it("handles single-character command", () => {
      expect(buildTelegramNativeCommandCallbackData("/x")).toBe("tgcmd:/x");
    });

    it("handles unicode-free command arguments", () => {
      expect(buildTelegramNativeCommandCallbackData("/broadcast Hello world")).toBe(
        "tgcmd:/broadcast Hello world",
      );
    });
  });

  // -------------------------------------------------------------------------
  // parseTelegramNativeCommandCallbackData
  // -------------------------------------------------------------------------

  describe("parseTelegramNativeCommandCallbackData", () => {
    it("extracts slash command from tgcmd: prefix", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd:/help")).toBe("/help");
    });

    it("returns null for non-slash text after tgcmd: prefix", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd:status")).toBeNull();
    });

    it("returns null for non-tgcmd callback data", () => {
      expect(parseTelegramNativeCommandCallbackData("somecallbackdata")).toBeNull();
    });

    it("returns null for empty string", () => {
      expect(parseTelegramNativeCommandCallbackData("")).toBeNull();
    });

    it("returns null for null/undefined input", () => {
      expect(parseTelegramNativeCommandCallbackData(null)).toBeNull();
      expect(parseTelegramNativeCommandCallbackData(undefined)).toBeNull();
    });

    it("trims whitespace and extracts slash command", () => {
      expect(parseTelegramNativeCommandCallbackData("  tgcmd:/test  ")).toBe("/test");
    });

    it("handles command with arguments", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd:/model claude")).toBe(
        "/model claude",
      );
    });

    it("handles multiple slashes — only accepts leading slash", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd://help")).toBeNull();
    });

    it("is case-sensitive: non-matching prefix returns null", () => {
      expect(parseTelegramNativeCommandCallbackData("TGCMD:/help")).toBeNull();
    });

    it("accepts whitespace-only before tgcmd: prefix", () => {
      expect(parseTelegramNativeCommandCallbackData("  tgcmd:/start")).toBe("/start");
    });

    it("returns null when prefix is empty after stripping", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd:")).toBeNull();
    });

    it("returns null for slash-only text", () => {
      expect(parseTelegramNativeCommandCallbackData("tgcmd:/")).toBeNull();
    });
  });

  // -------------------------------------------------------------------------
  // Round-trip integration
  // -------------------------------------------------------------------------

  describe("round-trip: build → parse", () => {
    const commands = [
      "/help",
      "/status",
      "/model claude",
      "/export-session",
      "/start arg1 arg2",
      "/broadcast Hello world",
    ];

    it.each(commands)("round-trips '%s'", (command) => {
      const built = buildTelegramNativeCommandCallbackData(command);
      const parsed = parseTelegramNativeCommandCallbackData(built);
      expect(parsed).toBe(command);
    });

    it("round-trip only works for slash-prefixed commands", () => {
      const built = buildTelegramNativeCommandCallbackData("status");
      expect(parseTelegramNativeCommandCallbackData(built)).toBeNull();
    });
  });
});