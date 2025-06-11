def can_trust_message(message):
    charsUsed = set()
    for char in message:
        if char == " ":
            continue
        charsUsed.add(char)
    return len(charsUsed) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
