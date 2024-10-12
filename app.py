# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Define financial data for each company with additional metrics
company_data = {
    "apple": {
        "total_revenue": "$394,328 million",
        "net_income_change": "increased by $12,036 million over the last year",
        "profit_margin": "25%",
        "debt_to_asset_ratio": "85.71%",
        "total_assets_growth": "grown by 2.5% over the past year",
        "total_assets": "$351,002 million",
        "total_liabilities": "$287,056 million",
        "cash_flow": "$104,038 million",
        "net_income": "$94,680 million"
    },
    "microsoft": {
        "total_revenue": "$198,270 million",
        "net_income_change": "increased by $16,575 million over the last year",
        "profit_margin": "30%",
        "debt_to_asset_ratio": "65.42%",
        "total_assets_growth": "grown by 3.2% over the past year",
        "total_assets": "$286,556 million",
        "total_liabilities": "$187,322 million",
        "cash_flow": "$76,710 million",
        "net_income": "$72,537 million"
    },
    "tesla": {
        "total_revenue": "$81,462 million",
        "net_income_change": "increased by $5,519 million over the last year",
        "profit_margin": "10%",
        "debt_to_asset_ratio": "50.23%",
        "total_assets_growth": "grown by 4.8% over the past year",
        "total_assets": "$52,148 million",
        "total_liabilities": "$27,830 million",
        "cash_flow": "$5,974 million",
        "net_income": "$5,518 million"
    }
}


def simple_chatbot(company, user_query):
    company = company.lower()
    if company not in company_data:
        return "Sorry, I don't have data for that company."
    
    responses = company_data[company]
    
    # Normalize the user query for case-insensitive matching
    query = user_query.strip().lower()
    
    if "total revenue" in query:
        return f"The total revenue of {company.capitalize()} is {responses['total_revenue']}."
    elif "net income" in query or "total income" in query:
        return f"The net income of {company.capitalize()} is {responses['net_income']}."
    elif "profit margin" in query:
        return f"The current profit margin of {company.capitalize()} is {responses['profit_margin']}."
    elif "debt-to-asset ratio" in query or "debt to asset ratio" in query:
        return f"The debt-to-asset ratio of {company.capitalize()} is {responses['debt_to_asset_ratio']}."
    elif "total assets grown" in query or "total assets growth" in query:
        return f"Total assets of {company.capitalize()} have {responses['total_assets_growth']}."
    elif "total assets" in query:
        return f"The total assets of {company.capitalize()} are {responses['total_assets']}."
    elif "total liabilities" in query:
        return f"The total liabilities of {company.capitalize()} are {responses['total_liabilities']}."
    elif "cash flow" in query:
        return f"The cash flow of {company.capitalize()} is {responses['cash_flow']}."
    else:
        return "Sorry, I can only provide information on predefined queries."


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    query = ""
    company = ""
    if request.method == "POST":
        company = request.form.get("company", "").strip()
        query = request.form.get("query", "").strip()
        if company and query:
            response = simple_chatbot(company, query)
        else:
            response = "Please enter both company name and your query."
    return render_template("index.html", response=response, query=query, company=company)

if __name__ == "__main__":
    app.run(debug=True)
