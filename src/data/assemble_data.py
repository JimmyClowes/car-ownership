import requests
import src.utils.git as gitutil

# determine top level project directory
bpath = gitutil.get_root()


def fetch_data_source(target_url,
                      output_file):
    """Fetch raw data from source url and save locally.

    Args:
        target_url (str): URL determining source file containing raw data.
        output_file (str): Filepath within project directory (excluding path of directory itself)
    """
    
    r = requests.get(target_url, allow_redirects=True)

    with open(bpath + output_file, 'wb') as f:
        f.write(r.content)

if __name__ == '__main__':

    # fetch car ownership per area data
    fetch_data_source('https://data.london.gov.uk/download/licensed-vehicles-numbers-borough/45c47aba-682d-4be4-b62a-42215203c2ad/vehicles-licensed-borough.xls',
                      output_file = '/data/raw/ts_cars_area.xls')