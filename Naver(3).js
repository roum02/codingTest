import cx from "classnames";
import { Component } from "react";

export default class LikeDislike extends Component {
  render() {
    return (
      <>
        <div>
          <h2>Like/Dislike</h2>
        </div>
        <style>{`
                    .like-button, .dislike-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:   #585858;
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
