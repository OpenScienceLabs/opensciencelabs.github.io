from pathlib import Path
from typing import Optional

AUDIO_EXTS = {".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac"}
TEXT_EXTS = {".txt", ".md", ".srt", ".vtt", ".json"}


def _ext_of(path: Optional[str]) -> str:
    return Path(path).suffix.lower() if path else ""


def validate_io_paths(input_path: Optional[str], output_path: Optional[str], operation: Optional[str] = None) -> None:
    """
    Validate input/output extensions for common operations.

    operation can be:
      - 'text-to-speech' / 'text->speech' / 'tts'
      - 'speech-to-text' / 'speech->text' / 'stt'
      - None (best-effort inference)

    Raises ValueError on invalid combinations.
    """
    op = (operation or "").lower()
    in_ext = _ext_of(input_path)
    out_ext = _ext_of(output_path)

    tts_ops = {"text-to-speech", "text->speech", "tts"}
    stt_ops = {"speech-to-text", "speech->text", "stt"}

    if op in tts_ops:
        if not output_path or out_ext == "":
            raise ValueError("text->speech requires an audio output file (e.g. --output-path out.mp3).")
        if out_ext not in AUDIO_EXTS:
            raise ValueError(f"Invalid output audio format '{out_ext}'. Supported: {', '.join(sorted(AUDIO_EXTS))}")

    elif op in stt_ops:
        if not input_path or in_ext == "" or in_ext not in AUDIO_EXTS:
            raise ValueError(f"speech->text requires an audio input file (supported: {', '.join(sorted(AUDIO_EXTS))}).")
        if not output_path or out_ext == "" or out_ext not in TEXT_EXTS:
            raise ValueError(f"speech->text requires a text output file (supported: {', '.join(sorted(TEXT_EXTS))}).")

    else:
        # Infer operation by extensions and validate.
        inferred_op = None
        if in_ext:
            if in_ext in AUDIO_EXTS:
                inferred_op = "speech-to-text"
            elif in_ext in TEXT_EXTS:
                inferred_op = "text-to-speech"
        if not inferred_op and out_ext:
            if out_ext in AUDIO_EXTS:
                inferred_op = "text-to-speech"
            elif out_ext in TEXT_EXTS:
                inferred_op = "speech-to-text"

        if inferred_op == "text-to-speech":
            if not output_path or out_ext == "":
                raise ValueError("text->speech requires an audio output file (e.g. --output-path out.mp3).")
            if out_ext not in AUDIO_EXTS:
                raise ValueError(f"Invalid output audio format '{out_ext}'. Supported: {', '.join(sorted(AUDIO_EXTS))}")
        elif inferred_op == "speech-to-text":
            if not input_path or in_ext == "" or in_ext not in AUDIO_EXTS:
                raise ValueError(f"speech->text requires an audio input file (supported: {', '.join(sorted(AUDIO_EXTS))}).")
            if not output_path or out_ext == "" or out_ext not in TEXT_EXTS:
                raise ValueError(f"speech->text requires a text output file (supported: {', '.join(sorted(TEXT_EXTS))}).")
        else:
            if input_path and in_ext and in_ext not in AUDIO_EXTS.union(TEXT_EXTS):
                raise ValueError(f"Unsupported input extension '{in_ext}'. Supported: audio {', '.join(sorted(AUDIO_EXTS))} or text {', '.join(sorted(TEXT_EXTS))}.")
            if output_path and out_ext and out_ext not in AUDIO_EXTS.union(TEXT_EXTS):
                raise ValueError(f"Unsupported output extension '{out_ext}'. Supported: audio {', '.join(sorted(AUDIO_EXTS))} or text {', '.join(sorted(TEXT_EXTS))}.")

from pathlib import Path
from typing import Optional

AUDIO_EXTS = {".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac"}
TEXT_EXTS = {".txt", ".md", ".srt", ".vtt", ".json"}


def _ext_of(path: Optional[str]) -> str:
    return Path(path).suffix.lower() if path else ""


def validate_io_paths(input_path: Optional[str], output_path: Optional[str], operation: Optional[str] = None) -> None:
    """
    Validate input/output extensions for common operations.

    operation can be:
      - 'text-to-speech' / 'text->speech' / 'tts'
      - 'speech-to-text' / 'speech->text' / 'stt'
      - None (best-effort inference)

    Raises ValueError on invalid combinations.
    """
    op = (operation or "").lower()
    in_ext = _ext_of(input_path)
    out_ext = _ext_of(output_path)

    tts_ops = {"text-to-speech", "text->speech", "tts"}
    stt_ops = {"speech-to-text", "speech->text", "stt"}

    if op in tts_ops:
        if not output_path or out_ext == "":
            raise ValueError("text->speech requires an audio output file (e.g. --output-path out.mp3).")
        if out_ext not in AUDIO_EXTS:
            raise ValueError(f"Invalid output audio format '{out_ext}'. Supported: {', '.join(sorted(AUDIO_EXTS))}")

    elif op in stt_ops:
        if not input_path or in_ext == "" or in_ext not in AUDIO_EXTS:
            raise ValueError(f"speech->text requires an audio input file (supported: {', '.join(sorted(AUDIO_EXTS))}).")
        if not output_path or out_ext == "" or out_ext not in TEXT_EXTS:
            raise ValueError(f"speech->text requires a text output file (supported: {', '.join(sorted(TEXT_EXTS))}).")

    else:
        # Infer operation by extensions and validate.
        inferred_op = None
        if in_ext:
            if in_ext in AUDIO_EXTS:
                inferred_op = "speech-to-text"
            elif in_ext in TEXT_EXTS:
                inferred_op = "text-to-speech"
        if not inferred_op and out_ext:
            if out_ext in AUDIO_EXTS:
                inferred_op = "text-to-speech"
            elif out_ext in TEXT_EXTS:
                inferred_op = "speech-to-text"

        if inferred_op == "text-to-speech":
            if not output_path or out_ext == "":
                raise ValueError("text->speech requires an audio output file (e.g. --output-path out.mp3).")
            if out_ext not in AUDIO_EXTS:
                raise ValueError(f"Invalid output audio format '{out_ext}'. Supported: {', '.join(sorted(AUDIO_EXTS))}")
        elif inferred_op == "speech-to-text":
            if not input_path or in_ext == "" or in_ext not in AUDIO_EXTS:
                raise ValueError(f"speech->text requires an audio input file (supported: {', '.join(sorted(AUDIO_EXTS))}).")
            if not output_path or out_ext == "" or out_ext not in TEXT_EXTS:
                raise ValueError(f"speech->text requires a text output file (supported: {', '.join(sorted(TEXT_EXTS))}).")
        else:
            if input_path and in_ext and in_ext not in AUDIO_EXTS.union(TEXT_EXTS):
                raise ValueError(f"Unsupported input extension '{in_ext}'. Supported: audio {', '.join(sorted(AUDIO_EXTS))} or text {', '.join(sorted(TEXT_EXTS))}.")
            if output_path and out_ext and out_ext not in AUDIO_EXTS.union(TEXT_EXTS):
                raise ValueError(f"Unsupported output extension '{out_ext}'. Supported: audio {', '.join(sorted(AUDIO_EXTS))} or text {', '.join(sorted(TEXT_EXTS))}.")