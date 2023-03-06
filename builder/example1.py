if __name__ == "__main__":
    text = "hello"
    parts = ["<p>", text, "</p>"]
    print("".join(parts))

    words = ["hello", "world"]
    parts = ["<url>"]
    for w in words:
        parts.append(f" <li>{w}</li>")
    parts.append("</ul>")
    print("\n".join(parts))
