class product:
    def __init__(self, OriginalPrice: float, AfterPrice: float) -> None:
        self.OriginalPrice = OriginalPrice
        self.AfterPrice = AfterPrice
        self.PriceDiff = self.AfterPrice - self.OriginalPrice

    def percentage(self) -> float:
        return round(
            abs((NeoProduct.OriginalPrice - NeoProduct.AfterPrice) / self.OriginalPrice)
            * 100,
            2,
        )


NeoProduct = product(float(input("Preço original: ")), float(input("Preço agora: ")))
if NeoProduct.PriceDiff < 0:
    print(f"Desconto de {NeoProduct.percentage()}%.")
elif NeoProduct.PriceDiff > 0:
    print(f"Juros de {NeoProduct.percentage()}%.")
else:
    print("Mesmo preço!")
