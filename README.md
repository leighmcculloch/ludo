# Junior Ludo Game

A static website implementation of Junior Ludo that four players can use on a shared device.

## Features

- 🎲 Complete Junior Ludo game for 4 players
- 🤖 Automatic move detection when only one valid action is available
- 🎯 Turn-based gameplay on a shared device
- 📱 Responsive design that works on mobile and desktop
- ⚡ Single HTML file with inline CSS and JavaScript
- 🚀 Deno web server for local hosting

## How to Play

1. **Roll the Dice**: Click "Roll Dice" to start your turn
2. **Move Pieces**: Click on a piece to move it (when multiple pieces can move)
3. **Get Out of Home**: Roll a 6 to move pieces out of the home area
4. **Capture Opponents**: Land on opponent pieces to send them back home
5. **Win the Game**: Get all 4 pieces to the center to win!

### Junior Ludo Rules

- Each player has 4 pieces starting in their home area
- Roll a 6 to move pieces out of home onto the board
- Move pieces clockwise around the board
- Landing on an opponent's piece sends it back to their home
- Rolling a 6 gives you another turn
- Rolling three 6s in a row loses your turn
- First player to get all pieces to the center wins

## Running the Game

### Option 1: Open HTML File Directly
Simply open `index.html` in your web browser.

### Option 2: Using Deno Server (Recommended)
1. Install [Deno](https://deno.land/) if you haven't already
2. Run the server:
   ```bash
   deno run --allow-net --allow-read server.ts
   ```
3. Open http://localhost:8000 in your browser

### Option 3: Using Python Server (Alternative)
1. Run the Python server:
   ```bash
   python3 server.py
   ```
2. Open http://localhost:8001 in your browser

### Option 4: Using Basic Python HTTP Server
```bash
python3 -m http.server 8000
```
Then open http://localhost:8000 in your browser.

## Game Features

- **Automatic Moves**: When only one piece can move, it moves automatically
- **Visual Feedback**: Pieces that can move are highlighted and animated
- **Responsive Design**: Works on both desktop and mobile devices
- **Game State Management**: Tracks turns, dice rolls, and win conditions
- **Capture System**: Opponent pieces are sent back to home when captured
- **Safe Squares**: Special squares where pieces are safe from capture

## Development

The game is built with:
- **HTML5**: Structure and layout
- **CSS3**: Styling, animations, and responsive design
- **Vanilla JavaScript**: Game logic and interaction
- **Deno**: Web server for local hosting

All code is contained in a single HTML file (`index.html`) for easy deployment and sharing.
