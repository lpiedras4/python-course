string = ["Coding", "For", "All"]
result = " ".join(string)
company = "Apple"
print(' '.join(string))
print(len(company))
print(company.upper())
print(company.lower())
print(result.capitalize())
print(result.title())
print(result.swapcase())
print(string[slice(0)])
print(result.find("or"))
print(result.find("a"))
new_string = result.replace("Coding","Python")
print(new_string)
print(new_string.replace("For All","For Everyone"))
print(result.split(","))
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))