# ...existing code...
from artbox.validators import validate_io_paths
import sys
# ...existing code...

# INSERT: extract common arg names and validate extensions
input_path = getattr(args, "input_path", None) or getattr(args, "input", None) or None
output_path = getattr(args, "output_path", None) or getattr(args, "output", None) or None

operation = None
for attr in ("operation", "op", "command", "cmd", "subcommand", "mode"):
    val = getattr(args, attr, None)
    if isinstance(val, str) and val:
        operation = val
        break

if isinstance(operation, str):
    ol = operation.lower()
    if ol in ("tts", "text-to-speech", "text->speech"):
        operation = "text-to-speech"
    elif ol in ("stt", "speech-to-text", "speech->text"):
        operation = "speech-to-text"

try:
    validate_io_paths(input_path, output_path, operation)
except ValueError as e:
    print(f"Error: {e}", file=sys.stderr)
    raise SystemExit(2)
# ...existing code...