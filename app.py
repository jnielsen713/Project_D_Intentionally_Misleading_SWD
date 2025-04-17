# Imports --------------------------------------------------------------------------------------------------------------
from main import app
import layout
import plotly.graph_objects as go
import callbacks

# App Layout -----------------------------------------------------------------------------------------------------------

app.layout = layout.create_layout()
callbacks.register_callbacks(app)

# Run ------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)