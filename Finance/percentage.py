class product:
    def __init__(self, OriginalPrice: float, AfterPrice: float) -> None:
        self.OriginalPrice = OriginalPrice
        self.AfterPrice = AfterPrice

    def percentage(self) -> float:
        return round(
            abs((NeoProduct.OriginalPrice - NeoProduct.AfterPrice) / self.OriginalPrice)
            * 100,
            2,
        )


NeoProduct = product(float(input("Original price: ")), float(input("Price now: ")))
if NeoProduct.OriginalPrice - NeoProduct.AfterPrice < 0:
    print(f"Juros de {NeoProduct.percentage()}%.")
elif NeoProduct.OriginalPrice - NeoProduct.AfterPrice == 0:
    print("No difference!")
else:
    print(f"Desconto de {NeoProduct.percentage()}%.")
