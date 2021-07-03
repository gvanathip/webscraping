url = "http://www.thaifeedmill.com/tabid/78/Default.aspx"

import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
import datetime
import pandas as pd

ct = datetime.datetime.now()

print(datetime.datetime.now())