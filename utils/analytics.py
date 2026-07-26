import plotly.express as px


def expense_pie(category_data):

    fig = px.pie(
        values=category_data.values,
        names=category_data.index,
        hole=0.45
    )

    fig.update_layout(
        title="Expense Distribution",
        template="plotly_white"
    )

    return fig


def expense_bar(category_data):

    fig = px.bar(
        x=category_data.index,
        y=category_data.values
    )

    fig.update_layout(
        title="Expenses by Category",
        xaxis_title="Category",
        yaxis_title="Amount",
        template="plotly_white"
    )

    return fig