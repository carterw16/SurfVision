import requests
from pysurfline import SpotForecast, SurfReport
import matplotlib.pyplot as plt

params = {
    "spotId": "5842041f4e65fad6a7708890",
    "days": 3,
    "intervalHours": 3,
}
report = SurfReport(params)

f=report.plot()
plt.show()
