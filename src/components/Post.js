import React from 'react';

export class Post extends React.Component {
  state = {
    opened: false
  }
  handleOpen = () => {
    this.setState((prevState) => ({ opened: !prevState.opened }));
  }
  render() {
    return (
      <div className='post'>
        <h2
          className='post__title'
          onClick={this.handleOpen}
        >
          {this.props.postName}
        </h2>
        {this.state.opened && <div className='post__body'>
          <h3 className='post__address'>{this.props.postAddress}</h3>
          <p className='post__entry'>{this.props.postEntry}</p>
        </div>}
      </div>
    )
  }
}
export default Post;