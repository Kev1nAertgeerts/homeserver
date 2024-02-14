import plotly.graph_objects as go

class Plot:
    def pie_chart_available(self, balance):
        labels = []
        available = []
        for i in balance:
            labels.append(i["symbol"])
            available.append(i["value"])
        fig_available = go.Figure(data=[go.Pie(labels=labels, values=available, textinfo='label+percent',insidetextorientation='radial')])
        fig_available_html = fig_available.to_html()
        return fig_available_html
    
    def pie_chart_inorder(self, balance):
        labels = []
        inorder = []
        for i in balance:
            labels.append(i["symbol"])
            inorder.append(i["inOrder"])
        fig_inorder = go.Figure(data=[go.Pie(
            labels=labels, values=inorder, textinfo='label+percent', insidetextorientation='radial')])
        fig_inorder_html = fig_inorder.to_html()
        return fig_inorder_html
