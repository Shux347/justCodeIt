import React from "react";
import "./style.css";

function App() {
  return (
    <div className="screen">
      {/* Header */}
      <div id="front">
        <div className="logo">
          <img
            src="https://scontent.xx.fbcdn.net/v/t1.15752-9/411196255_348578967886806_2830647330875243308_n.png?_nc_cat=101&ccb=1-7&_nc_sid=510075&_nc_eui2=AeEafSBI9Cn3S5g4vpmTSrFS-2SBgE57uwX7ZIGATnu7BW5InYlzAbEU6CVPQl6MSHlfjLNfsJq7stPsMrEk9LmA&_nc_ohc=eNa54ME05UgAX_hyxQT&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdSmU2aVU8Gk0IU4i4kCcWFQ0pdyvyDpPLx7jwbVFDv_0w&oe=65B26521"
            style={{ width: "36%", height: "86px" }}
            alt="Lib.d logo"
          />
        </div>
        <div id="srch"></div>
      </div>

      {/* Navigation */}
      <div className="nav">
        <a className="link1" href="#front">
          <div className="box1">
            <p>Home</p>
          </div>
        </a>

        <a className="link2" href="#products">
          <div className="box2">
            <p>Products</p>
          </div>
        </a>

        <a className="link3" href="#vouchers">
          <div className="box3">
            <p>Vouchers</p>
          </div>
        </a>

        <a className="link4" href="#catalogue">
          <div className="box4">
            <p>Catalogue</p>
          </div>
        </a>
      </div>

      {/* Feature image */}
      <div id="feature">
        <img
          src="https://i.pinimg.com/564x/36/a0/85/36a085785eabcc6add04d35e8c97be37.jpg"
          alt="Featured Book"
          style={{ width: "100%", height: "450px" }}
        />
      </div>

      {/* "Shop Now" button */}
      <a className="anm" href="#products">
        Shop Now!
      </a>

      {/* Products Section */}
      <div id="products">
        <h3>Latest Products</h3>

        <div className="product-1">
          <div className="img1">
            <img className="pjo" alt="Percy Jackson" />
          </div>
          <p>
            Percy Jackson and the Olympiad
            <br />
            P1,109.00
          </p>
        </div>

        <div className="product-2">
          <div className="img2">
            <img className="hg" alt="Hunger Games" />
          </div>
          <p>
            The Hunger Games Trilogy
            <br />
            P1,499.00
          </p>
        </div>

        <div className="product-3">
          <div className="img3">
            <img className="pwr" alt="48 Laws of Power" />
          </div>
          <p>
            The 48 Laws of Power
            <br />
            P1,299.00
          </p>
        </div>

        <div className="product-4">
          <div className="img4">
            <img className="kll" alt="To Kill a Mockingbird" />
          </div>
          <p>
            To Kill a Mockingbird
            <br />
            P450.00
          </p>
        </div>

        <div className="product-5">
          <div className="img5">
            <img className="miss" alt="Miss Peregrine's Home" />
          </div>
          <p>
            Miss Peregrine's Home for Peculiar Children
            <br />
            P1,995.00
          </p>
        </div>

        <div className="product-6">
          <div className="img6">
            <img className="wmn" alt="Little Women" />
          </div>
          <p>
            Little Women
            <br />
            P325.00
          </p>
        </div>

        <div className="product-7">
          <div className="img7">
            <img className="crws" alt="Six of Crows" />
          </div>
          <p>
            Six of Crows
            <br />
            P645.00
          </p>
        </div>

        <div className="product-8">
          <div className="img8">
            <img className="prd" alt="Pride and Prejudice" />
          </div>
          <p>
            Pride and Prejudice
            <br />
            P145.00
          </p>
        </div>
      </div>

      {/* About Us Section (vouchers ID but states About Us) */}
      <div id="vouchers">
        <h4>About Us</h4>
        <p>
          Lib.d is an online shopping web page to offer the best to you.
          To give you the best books to read so you can live your life
          without regrets.
        </p>
        <div className="img-vouchers">
          <img
            src="https://i.pinimg.com/564x/a2/6a/27/a26a27a5ff6a2cb80d5b872a73d1413b.jpg"
            alt="About Lib.d"
            style={{ height: "335px" }}
          />
        </div>
      </div>

      {/* Catalogue Section */}
      <div id="catalogue">
        <div className="label">
          <h5>catalogue us!</h5>
        </div>
        <p>
          Gmail: noname@gmail.com <br />
          Lazada: Lib.d Official Store <br />
          Shoppee: Lib.d Official Store <br />
          Facebook page: Lib.d Bookstore <br />
          catalogue no. : +63 9863 656 8354
        </p>
      </div>
    </div>
  );
}

export default App;
