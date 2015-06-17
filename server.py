from brave.app.app import app
from brave.config.application import applicationWillLunch
from brave.models.deal import DealRecord
if __name__ == '__main__':
    applicationWillLunch()
    app.run(host="172.22.155.27", debug=True)
