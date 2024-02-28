def ArithmeticProgression(iTerm, fTerm, constant):
    listTerms = []

    if constant < 1 and iTerm > fTerm:
        while iTerm >= fTerm:
            listTerms.append(iTerm)
            iTerm = iTerm * constant
    elif constant >= 1 and iTerm < fTerm:
        while iTerm < fTerm:
            listTerms.append(iTerm)
            iTerm = iTerm * constant
    else:
        return listTerms

    return listTerms


initialTerm = float(input("Fist term: "))
finalTerm = float(
    input("Last term: ")
)  # depending on the constant may not be the last term
constant = float(input("Constant: "))

print(
    ArithmeticProgression(initialTerm, finalTerm, constant),
    f"Size of {len(ArithmeticProgression(initialTerm, finalTerm, constant))}.",
)
