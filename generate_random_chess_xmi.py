import random
import uuid
import argparse

def generate_piece_instance(piece_type, color, row, col, index):
    name = f"{piece_type}_{color}_{row}_{col}"
    piece_id = f"_{uuid.uuid4().hex[:8]}"
    return f"""
    <packagedElement xmi:type=\"uml:InstanceSpecification\" xmi:id=\"{piece_id}\" name=\"{name}\">
        <classifier href=\"#_{piece_type}_class_id\"/>
    </packagedElement>""".strip()

def generate_random_chess_xmi(piece_count=10):
    piece_types = ["Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]
    colors = ["White", "Black"]
    positions = [(row, col) for row in range(1, 9) for col in range(1, 9)]
    random.shuffle(positions)
    selected_positions = positions[:piece_count]

    pieces = []
    for i, (row, col) in enumerate(selected_positions):
        piece_type = random.choice(piece_types)
        color = random.choice(colors)
        pieces.append(generate_piece_instance(piece_type, color, row, col, i))

    body = "\n".join(pieces)
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    xml += "<uml:Model xmi:version=\"20131001\"\n"
    xml += "    xmlns:xmi=\"http://www.omg.org/spec/XMI/20131001\"\n"
    xml += "    xmlns:uml=\"http://www.eclipse.org/uml2/5.0.0/UML\"\n"
    xml += "    xmi:id=\"model_random\" name=\"random_board\">\n"
    xml += body + "\n</uml:Model>"
    return xml

def main():
    parser = argparse.ArgumentParser(description="Generate random XMI chessboard.")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of pieces to place")
    parser.add_argument("-o", "--output", type=str, default="random_chess_board.xmi", help="Output file name")
    args = parser.parse_args()

    content = generate_random_chess_xmi(args.number)
    with open(args.output, "w") as f:
        f.write(content)
    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
