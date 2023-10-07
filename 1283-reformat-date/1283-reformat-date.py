class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict={
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
        "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        datep= date.split()
        day = datep[0][:-2]
        month = month_dict[datep[1]]
        year = datep[2]
        day = day.zfill(2)
        res= f"{year}-{month}-{day }"
        return res