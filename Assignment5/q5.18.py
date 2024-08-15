class Tender:
    def __init__(self, cost, company_name):
        self.cost = cost
        self.company_name = company_name
if __name__ == "__main__":
    tenders = []
    for i in range(5):
        company_name = input(f"Enter company name for tender {i + 1}: ")
        cost = float(input(f"Enter cost for tender {i + 1}: "))
        tenders.append(Tender(cost, company_name))
    min_cost_tender = min(tenders, key=lambda t: t.cost)
    print(f"The company with the minimum cost is: {min_cost_tender.company_name}")
