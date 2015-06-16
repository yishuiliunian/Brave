from brave.app.app import app
from brave.config.application import applicationWillLunch
from brave.models.deal import DealRecord
if __name__ == '__main__':
    applicationWillLunch()
    app.run(debug=True)
