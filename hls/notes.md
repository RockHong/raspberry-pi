## web page
- bootstrap
- jquery
- less

### html
[&lt;video&gt;][3]


## http live streaming
Apple documents: [doc 1][1], [doc 2][2]

### mediafilesegmenter
命令示例，

	mediafilesegmenter -f www-root/v/test-1/ -b http://localhost:8080/v/test-1/ IMG_2146.m4v

### iframe\_index.m3u8 or prog\_index.m3u8
苹果文档说`iframe_index.m3u8`能更好地支持快进、后退。
但是`http://localhost:8080/v/test-1/iframe_index.m3u8`貌似不能工作，
而`http://localhost:8080/v/test-1/prog_index.m3u8`可以正常播放。

TODO





[1]: https://developer.apple.com/streaming/ "http live streaming"
[2]: https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html "http live streaming"
[3]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video "video tag"
