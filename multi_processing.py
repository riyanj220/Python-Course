import requests


def download_file(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
            print(f"downloaded file {file_name}")

    else:
        print(f"failed to downlaod {url}")


url = "https://fastly.picsum.photos/id/29/4000/2670.jpg?hmac=rCbRAl24FzrSzwlR5tL-Aqzyu5tX_PA95VJtnUXegGU"
file_name = "test.jpg"

download_file(url, file_name)


# _______________________________________________________________________
# import multiprocessing
# import requests


# def download_file(url, name):
#     print(f"started downloading {name}")
#     response = requests.get(url)
#     open(f"file {name}.jpg", "wb").write(response.content)

#     print(f"finished downloading {name}")


# if __name__ == "__main__":
#     url = "https://picsum.photos/2000/3000"
#     pros = []

#     for i in range(5):
#         p = multiprocessing.Process(target=download_file, args=[url, i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()
