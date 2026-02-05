#1
# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("hello, i am so tired")

#2
# with open("test.txt", "r", encoding="utf-8") as file:
#     content=file.read()
#     print(f"file content:{content}")
#     print(f"symbols:{len(content)}")
# #
# #3
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("\nthis is another text")
# #
# #4
# with open("test.txt", "r", encoding="utf-8") as source:
#     data=source.read()
#
# with open("copy_test.txt", "w", encoding="utf-8") as destination:
#     destination.write(data)
#
# #6
# with open("test.txt", "r", encoding="utf-8") as file:
#     content=file.read()
#     print(content.upper())
#
# #7
with open("data.txt", "w", encoding="utf-8") as file:
    print("enter text, for ending type 0")
    while True:
        user_input=input()
        if user_input==0:
            break
