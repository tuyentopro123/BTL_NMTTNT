import "./Header.css";
import Icon from "../../img/Logo_PTIT_University.png"
import bng from "../../img/background.jpg"
import { Link } from "react-router-dom";

const Header = () => {
    const navbar = [
        {
          h4: "Phân loại văn bản",
          path: "/",
        },
        {
          h4: "Phân tích dữ liệu",
          path: "/classify",
        },
        // {
        //   h4: "Phân tích kết quả",
        //   path: "/about",
        // },
      ];
  return (
      <main className="header">
        <div className="header_bg" style={{backgroundImage: `url(${bng})`}}>
            <div className="header_icon">
                <img src={Icon} alt="" />
                <div className="school">
                    <h1>Học viện Công Nghệ Bưu chính viễn thông</h1>
                    <p>Post and Telecommunications Institute of Technology</p>
                </div>
            </div>
            <div className="header_info">
                <div className="header_container">
                    <div className="header_title">Phân loại tin tức</div>
                    <div className="header_group">Nhóm: 21</div>
                    <div className="header_member">GVHD: Nguyễn Thị Mai Trang</div>
                </div>
            </div>
        </div>
        <div className="header_navbar">
            <div className="navbar_container">
            {navbar.map((item, index) => (
                <Link
                    to={`${item.path}`}
                    key={index}
                    className={`navbar_item`}
                    style={{textDecoration: "none"}}
                >
                    <h4>{item.h4}</h4>
                </Link>
                ))}
            </div>
        </div>
      </main>
  );
};

export default Header;
