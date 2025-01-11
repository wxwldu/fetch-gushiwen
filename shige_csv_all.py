import os
from shige import fetch_html, extract_poem_urls, fetch_poem_details,get_title_categroy,extract_poem_urls_categroy


def get_url_categroy_11():
     url = 'https://www.gushiwen.cn/shiwens/'
     poem_urls_categroy = []
     html_content = fetch_html(url)
     if html_content:
        poem_urls_categroy.extend(extract_poem_urls_categroy(html_content))
     else:
        print("Failed to fetch or parse HTML content.")
    # print(f"{len(poem_urls_categroy)} Total {poem_urls_categroy} poem URLs.")
    # print(get_title_categroy(poem_urls_categroy[0]))
     for aurl in poem_urls_categroy:
         poem_urls = []
        #  print(f"{len(poem_urls_categroy)} Total {aurl} poem URLs.")
     return poem_urls_categroy

if __name__ == "__main__":
    urls_categroy = []
    for aurl in get_url_categroy_11():
         modified_string = aurl.replace("https://gushiwen", "https://www.gushiwen")
         urls_categroy.append(modified_string)
        #  print(f"{urls_categroy}Total {modified_string} poem URLs.")
        
    for url in urls_categroy:
    # url = "https://www.gushiwen.cn/gushi/chuci.aspx"
    # print(f"Total {urls_categroy} poem URLs.")
            currentUrl = url
            poem_urls = []
            print(currentUrl)
            html_content = fetch_html(currentUrl)
            if html_content:
                poem_urls.extend(extract_poem_urls(html_content))
            else:
                print("Failed to fetch or parse HTML content.")
            title_category = get_title_categroy(currentUrl)
            file_path = f"{title_category}.csv"
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(
                        "name,type,author,dynasty,content,trans,annotation,appreciation,background\n"
                    )
            else:
                #跳过该循环
                continue
            for url in poem_urls:
                details = fetch_poem_details(url)
                with open(file_path, "a", encoding="utf-8") as f:
                    print(f"Writing details for poem: {details['name']}")
                    for key in details:
                        details[key] = details[key].replace("\xa0", "")
                    f.write(
                        f"{details['name']},{title_category},{details['author']},{details['dynasty']},{details['content']},{details['trans']},{details['annotation']},{details['appreciation']},{details['background']}\n"
                    )





# import os
# from shige import fetch_html, extract_poem_urls, fetch_poem_details,extract_poem_urls_categroy,get_title_categroy


# # file_path = "poems.csv"

# def get_url_categroy_11():
#      url = 'https://www.gushiwen.cn/shiwens/'
#      poem_urls_categroy = []
#      html_content = fetch_html(url)
#      if html_content:
#         poem_urls_categroy.extend(extract_poem_urls_categroy(html_content))
#      else:
#         print("Failed to fetch or parse HTML content.")
#     # print(f"{len(poem_urls_categroy)} Total {poem_urls_categroy} poem URLs.")
#     # print(get_title_categroy(poem_urls_categroy[0]))
#      for aurl in poem_urls_categroy:
#          poem_urls = []
#         #  print(f"{len(poem_urls_categroy)} Total {aurl} poem URLs.")
#      return poem_urls_categroy


# if __name__ == "__main__":
#     aurl = get_url_categroy_11()[0]
#     html_content123 = fetch_html("https://www.gushiwen.cn/gushi/chuci.aspx")
#     print(aurl)
#     title_category = get_title_categroy("https://www.gushiwen.cn/gushi/chuci.aspx")
#     file_path = f"{title_category}.csv" 
#     print(file_path)
#     if not os.path.exists("file_path.csv"):
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(
#                 "name,author,dynasty,content,trans,annotation,appreciation,background\n"
#             )

#     url = aurl
#     poem_urls = []
#     html_content = fetch_html(url)
#     if html_content:
#         poem_urls.extend(extract_poem_urls(html_content))
#     else:
#         print("Failed to fetch or parse HTML content.")

#     for url in poem_urls:
#         details = fetch_poem_details(url)
#         with open(file_path, "a", encoding="utf-8") as f:
#             print(f"Writing details for poem: {details['name']}")
#             for key in details:
#                 details[key] = details[key].replace("\xa0", "")
#             f.write(
#                 f"{details['name']},{details['author']},{details['dynasty']},{details['content']},{details['trans']},{details['annotation']},{details['appreciation']},{details['background']}\n"
#             )


#     # for aurl in get_url_categroy():
#     #     title_category = get_title_categroy(aurl)
#     #     file_path = title_category + ".csv"
#     #     if not os.path.exists(file_path):
#     #         with open(file_path, "w", encoding="utf-8") as f:
#     #             f.write(
#     #                 "name,author,dynasty,content,trans,annotation,appreciation,background\n"
#     #             )

#     #     url = aurl
#     #     poem_urls = []
#     #     html_content = fetch_html(url)
#     #     if html_content:
#     #         poem_urls.extend(extract_poem_urls(html_content))
#     #     else:
#     #         print("Failed to fetch or parse HTML content.")

#     #     for url in poem_urls:
#     #         details = fetch_poem_details(url)
#     #         with open(file_path, "a", encoding="utf-8") as f:
#     #             print(f"Writing details for poem: {details['name']}")
#     #             for key in details:
#     #                 details[key] = details[key].replace("\xa0", "")
#     #             f.write(
#     #                 f"{details['name']},{details['author']},{details['dynasty']},{details['content']},{details['trans']},{details['annotation']},{details['appreciation']},{details['background']}\n"
#     #             )

            
    
# import os
# from shige import fetch_html, extract_poem_urls, fetch_poem_details,get_title_categroy



# if __name__ == "__main__":
#     url = "https://www.gushiwen.cn/gushi/chuci.aspx"
#     poem_urls = []
#     html_content = fetch_html(url)
#     if html_content:
#         poem_urls.extend(extract_poem_urls(html_content))
#     else:
#         print("Failed to fetch or parse HTML content.")


#     title_category = get_title_categroy(url)
#     file_path = f"{title_category}.csv"
#     if not os.path.exists(file_path):
#         with open(file_path, "w", encoding="utf-8") as f:
#             f.write(
#                 "name,author,dynasty,content,trans,annotation,appreciation,background\n"
#             )
#     for url in poem_urls:
#         details = fetch_poem_details(url)
#         with open(file_path, "a", encoding="utf-8") as f:
#             print(f"Writing details for poem: {details['name']}")
#             for key in details:
#                 details[key] = details[key].replace("\xa0", "")
#             f.write(
#                 f"{details['name']},{details['author']},{details['dynasty']},{details['content']},{details['trans']},{details['annotation']},{details['appreciation']},{details['background']}\n"
#             )
