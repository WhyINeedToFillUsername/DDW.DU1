import os
from scrapy import cmdline

output_file = "output.jl"
os.remove(output_file)
cmdline.execute(("scrapy crawl zive -o " + output_file).split())
# cmdline.execute("scrapy crawl regiojet -o output.jl".split())

# print('https://jizdenky.regiojet.cz/Booking/' +
# 'from/372825000/to/17655001/tarif/REGULAR/departure/20180404/retdep/20180404/return/false?5#search-results')