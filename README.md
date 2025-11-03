Chess Variant (Console)

Goals
- Play custom chess variants in the console end-to-end.
- Board size and piece definitions configurable via JSON.
- Detect check, legal moves, checkmate and stalemate.

Quick Start
1. Python 3.10+
2. Run: `python -m chess_variant.cli variants/standard.json`

Controls
- Input move as `e2e4` or `e2 e4`.
- `moves e2` lists legal moves from a square.
- `help`, `fen`, `board`, `quit`.

Variant Format (JSON)
- `name`: string
- `board`: `{ "width": int, "height": int }` (max 26 cols)
- `royal`: piece key for the royal piece (e.g., `K`)
- `pieces`: map of piece keys to definitions
- `setup`: array of strings from top rank to bottom rank, each of length = width, using piece keys; uppercase = white, lowercase = black, `.` = empty

Piece Definitions
- Sliding/leaper via `deltas` and `sliding`.
- Knight-like jumpers set `leaper: true`.
- Pawn-like pieces: `pawn: true`, with `move`, `attack` deltas (relative to side), optional `promote_to` (default `Q`).

Notes
- Castling and en passant are not yet implemented.
- Pawn promotion defaults to `Q` when reaching back rank.

