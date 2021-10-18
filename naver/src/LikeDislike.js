//import cx from "classnames";
import { Component } from "react";

export default class LikeDislike extends Component {
  constructor(props) {
    super(props);

    this.state = {
      like: 100,
      dislike: 25,
      bool: true,
    };
  }
  changeLikeAdd = () => {
    this.setState({
      like: 101,
      bool: false,
    });
  };

  changeLikeOrigin = () => {
    this.setState({
      like: 100,
      bool: true,
    });
  };

  changeDislikeAdd = () => {
    this.setState({
      dislike: 26,
      bool: false,
    });
  };

  changeDislikeOrigin = () => {
    this.setState({
      dislike: 25,
      bool: true,
    });
  };

  render() {
    return (
      <>
        <div>
          <h2>Like/Dislike</h2>
        </div>
        <>
          {this.state.bool ? (
            <button className="like-button" onClick={this.changeLikeAdd}>
              Like | {this.state.like}
            </button>
          ) : (
            <button className="like-button" onClick={this.changeLikeOrigin}>
              Like | {this.state.like}
            </button>
          )}
        </>
        <>
          {this.state.bool ? (
            <button className="dislike-button" onClick={this.changeDislikeAdd}>
              DisLike | {this.state.dislike}
            </button>
          ) : (
            <button className="like-button" onClick={this.changeDislikeOrigin}>
              DisLike | {this.state.dislike}
            </button>
          )}
        </>
        <style>{`
                    .like-button, .dislike-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:   #585858;
                        margin-right: 10px;
                    }

                    .liked, .disliked {
                        font-weight: bold;
                        color: #1565c0;
                    }
                `}</style>
      </>
    );
  }
}
