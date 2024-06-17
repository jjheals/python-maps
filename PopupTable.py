from folium import IFrame 


class PopupTable:
    
    popup_styles:str = ''' 
        <style>
            .popup-table {
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }
            .popup-table td, .popup-table th {
                border: 1px solid #ddd;
                padding: 8px;
            }
            .popup-table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .popup-table tr:hover {
                background-color: #ddd;
            }
            .popup-table th {
                padding-top: 12px;
                padding-bottom: 12px;
                text-align: left;
                background-color: #4CAF50;
                color: white;
            }
        </style>
    ''' 

    headers:list[str]       # The column headers 
    rows:list[list[str]]    # A 2D list containing the rows for the table
    table_html_class:str    # Optional specify the html class for the table 
    
    def __init__(self, headers:list[str], rows:list[list[str]], table_html_class:str='popup-table'):
        ''' Constructor for PopupTable. ''' 
        self.headers = headers
        self.rows = rows
        self.table_html_class = table_html_class

        
    def to_iframe(self) -> str:
        ''' Generates an IFrame for this popup table. ''' 
        
        # Create the HTML for the headers row
        headers_html:str = '<tr>' 
        for h in self.headers: headers_html += f'<th>{h}</th>'
        headers_html += '</tr>'
        
        # Create the HTML for each of the rows 
        rows_html:str = '' 
        
        # Iterate over the rows and create a new "<tr>" element for it
        for r in self.rows: 
            this_row_html:str = '<tr>'
            
            # Iterate over the cells in this row and create "<td>" cells for each 
            for c in r: this_row_html += f'<td>{c}</td>'
            
            # Append this row to the rows HTML
            rows_html += this_row_html
            
            # Closing tag for this row's tr element
            rows_html += '</tr>'
        
        # Construct the table HTML using the headers HTML and the rows HTML
        table_html:str = f''' 
            <table class="{self.table_html_class}">
                {headers_html}
                {rows_html}
            </table>
        '''
        
        # Define the table in HTML
        html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                {self.popup_styles}
            </head>
            <body>
                {table_html}
            </body>
            </html>
        '''
        
        # Create an IFrame with the HTML content
        iframe = IFrame(html, width=400, height=300)

        return iframe
    