import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Quản lý điểm")
#1 Dữ liệu 10 sinh viên
data={"Họ và tên":["Nguyễn Văn An","Trần Thái Bình","Lê Văn Chi",'Phạm Thị Dung','Hoàng Văn Hải','Vũ Thị Lan','Đỗ Văn Minh','Bùi Thị Nam','Ngô Văn Phúc','Dương Thị Trang'],
"Chuyên cần" :[8.0,9.0,7.5,8.5,6.0,9.5,7.0,8.0,6.5,9.0],
"Giữa Kỳ":[7.5,8.0,6.5,9.0,5.5,8.5,7.0,7.5,6.0,8.5],
"Cuối kỳ" :[8.0,8.5,7.0,8.5,5.0,9.0,6.5,8.0,6.0,8.5],}
df = pd.DataFrame(data)
df["Tong_ket"] =(0.2*df["Chuyên cần"])+(0.3*df["Giữa kỳ"])+(0.5*df["Cuối kỳ"])
df["Tong_ket"]= df['Tong_ket'].round(2)
def xep_loai(diem):
 if diem >=8.5:
   return"Giỏi"
 elif diem >=7.0:
   return"Khá"
 elif diem >=5.0:    
   return"Trung Bình"
 else:
    return"Yếu"
df["Xếp loại"]=df["Tong_ket"].apply(xep_loai)
st.dataframe(df)
#1 Hiện Thị Bảng Điểm
st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)
#2 Thống kê kết quả 
st.subheader("Thống kê kết quả học tập của lớp")
dtb_lop = df["Tong_ket"].mean()
max_lop = df["Tong_ket"].max()
min_lop = df["Tong_ket"].min()
so_sv_dat = (df["Tong_ket"]>=5.0).sum()
st.write(f"Điểm trung bình lớp:,{dtb_lop:.2f}")
st.write(f"Điểm cao nhất lớp:{max_lop}")
st.write(f"Điểm thấp nhất lớp:{min_lop}")
st.write(f"Số lượng sinh viên đạt(điểm tổng kết>=5.0):{so_sv_dat}sinh viên")
#3 Tra cứu theo sinh viên
st.subheader("Tra cứu điểm theo sinh viên")
selected_student =st.selectbox("Chọn sinh viên cần tra cứu",df["Họ và tên"])
student_info = df[df["Họ và tên"] == selected_student].iloc[0]
st.markdown(f"Họ và tên: {student_info['Họ và tên']}")
st.markdown(f"Điểm chuyên cần: {student_info['Chuyên cần']}")
st.markdown(f"Điểm giữa kỳ: {student_info['Giữa kỳ']}")
st.markdown(f"Điểm cuối kỳ: {student_info['Cuối kỳ']}")
st.markdown(f"Tổng kết: {student_info['Tổng kết']}")
st.markdown(f"Xếp loại: {student_info['Xếp loại']}")
#4 Biểu đồ cột
st.subheader("Biểu đồ cột thể hiện tổng kết của từng sinh viên")
fig,ax = plt.subplots(figsize(10,5))
ax.bar(df["Họ và tên"],df["Tổng kết"],color="skyblue",edgecolor="black")
ax.set_title("Biểu đồ thể hiện điểm tổng kết")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Tổng kết")
ax.set_ylim(0,10)
plt.xticks(rotation=30,ha ="right")
ax.grid(axis="y",linestyle="--",alpha=0.7)
st.pyplot(fig)
#5 Thông tin người tạo
st.markdown("---")
st.markdown("<p style='font-size:12px;colour:gray;'>Người tạo ứng dụng:Phan Văn Hoài Nam</p>",unsafe_allow_html=True)
