download install bootstrap jquery



### hls cmd
  591  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy test.mp4
  636  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy -b output test.mp4
  638  history | grep mediafilesegmenter
  639  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy test.mp4
  650  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy test.mp4
  654  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy -V test.mp4
  657  mediafilesegmenter -f output/ -i xxx.m3u8 -B yyy -b http://localhost:8080/output/  test.mp4
  659  mediafilesegmenter -f file-1/  -b http://localhost:8080/output/  test.mp4
  661  mediafilesegmenter -f file-1/  -b http://localhost:8080/output/  test.mp4
  671  history | grep filese


draft bash script--------------
output-dir=arg2
if output-dir exist; rm it
else mkdir output-dir

baseurl=arg3   #http://localhost:8080/v/

src=arg5  #IMG_2146.m4v

mediafilesegmenter -f $output-dir  -b $baseurl/$output-dir  $src

html-file=arg6
modify $html-file
-----------

### youtube 例子
youtube
<li class="yt-shelf-grid-item"><div class="yt-lockup yt-lockup-grid yt-lockup-video clearfix" data-context-item-id="PagVwAI9jao" data-visibility-tracking="CO4BEJQ1GAAiEwiC1-anmv7JAhVWYVgKHVvZBikojh5Aqpv2kYC4hdQ9"><div class="yt-lockup-dismissable"><div class="yt-lockup-thumbnail contains-addto">


<a aria-hidden="true" href="/watch?v=PagVwAI9jao" class="yt-uix-sessionlink        spf-link " data-sessionlink="itct=CO4BEJQ1GAAiEwiC1-anmv7JAhVWYVgKHVvZBikojh4yCmctaGlnaC1yZWM">
<div class="yt-thumb video-thumb">
<span class="yt-thumb-simple">
<img src="//i.ytimg.com/vi_webp/PagVwAI9jao/mqdefault.webp" alt="" width="196" height="110">  图片
</span>
</div>

<span class="video-time" aria-hidden="true">10:45</span>   视频时间

</a>  一个超链接

  <span class="thumb-menu dark-overflow-action-menu video-actions">
    <button class="yt-uix-button-reverse flip addto-watch-queue-menu spf-nolink hide-until-delayloaded yt-uix-button yt-uix-button-dark-overflow-action-menu yt-uix-button-size-default yt-uix-button-has-icon no-icon-markup yt-uix-button-empty" type="button" aria-haspopup="true" aria-expanded="false" onclick=";return false;"><span class="yt-uix-button-arrow yt-sprite"></span><ul class="watch-queue-thumb-menu yt-uix-button-menu yt-uix-button-menu-dark-overflow-action-menu hid"><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-next yt-uix-button-menu-item" data-action="play-next" onclick=";return false;" data-video-ids="PagVwAI9jao"><span class="addto-watch-queue-menu-text">Play next</span></li><li role="menuitem" class="overflow-menu-choice addto-watch-queue-menu-choice addto-watch-queue-play-now yt-uix-button-menu-item" data-action="play-now" onclick=";return false;" data-video-ids="PagVwAI9jao"><span class="addto-watch-queue-menu-text">Play now</span></li></ul></button>
  </span>


  <button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button video-actions spf-nolink hide-until-delayloaded addto-watch-later-button yt-uix-tooltip" type="button" onclick=";return false;" role="button" title="Watch Later" data-video-ids="PagVwAI9jao"></button>
  <button class="yt-uix-button yt-uix-button-size-small yt-uix-button-default yt-uix-button-empty yt-uix-button-has-icon no-icon-markup addto-button addto-queue-button video-actions spf-nolink hide-until-delayloaded addto-tv-queue-button yt-uix-tooltip" type="button" onclick=";return false;" title="Queue" data-video-ids="PagVwAI9jao" data-style="tv-queue"></button>
</div><div class="yt-lockup-content"><h3 class="yt-lockup-title contains-action-menu">
<a href="/watch?v=PagVwAI9jao" class="yt-uix-sessionlink  yt-ui-ellipsis yt-ui-ellipsis-2       spf-link " data-sessionlink="itct=CO4BEJQ1GAAiEwiC1-anmv7JAhVWYVgKHVvZBikojh4yCmctaGlnaC1yZWM" title="Bill Burr On Conan - Hilarious Interview - Star Wars - 12/16/2015" aria-describedby="description-id-292184" dir="ltr">Bill Burr On Conan - Hilarious Interview - Star Wars - 12/16/2015</a><span class="accessible-description" id="description-id-292184"> - Duration: 10:45.</span></h3><div class="yt-lockup-byline">by <a href="/user/reddevilan222" class="yt-uix-sessionlink g-hovercard      spf-link " data-ytid="UC6EGkZqfzH8wIky1O2FzZSQ" data-sessionlink="itct=CO4BEJQ1GAAiEwiC1-anmv7JAhVWYVgKHVvZBikojh4">Myron Putt</a></div><div class="yt-lockup-meta"><ul class="yt-lockup-meta-info"><li>235,624 views</li><li>1 week ago</li></ul></div>  <div class="yt-uix-menu-container yt-lockup-action-menu">
    
      <div class="yt-uix-menu yt-uix-menu-flipped hide-until-delayloaded">  <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-lockup-action-menu yt-uix-button-empty yt-uix-button-has-icon no-icon-markup  yt-uix-menu-trigger" type="button" onclick=";return false;" aria-pressed="false" aria-haspopup="true" role="button"><span class="yt-uix-button-arrow yt-sprite"></span></button>
<div class="yt-uix-menu-content yt-ui-menu-content yt-uix-menu-content-hidden" role="menu">  <ul>
      <li role="menuitem">
                <div class="service-endpoint-action-container hid">
                <div class="service-endpoint-replace-enclosing-action-notification hid">
          <div class="replace-enclosing-action-message">
            Video removed.
          </div>
          <div class="replace-enclosing-action-options">
                <button class="yt-uix-button yt-uix-button-size-default yt-uix-button-link undo-replace-action" type="button" onclick=";return false;" data-feedback-token="AB9zfpJsKANdZW4yMO5DIov2ZXbbieLU6VAKHkvAj1zzUNxz5dEPI8gJshIfjfvnMO-BRJoIdvh3EzJln_LheniTMubUtMfYgQjFR9am_Ll-BFlUzR_7WqyumxjZfBGMyDMhkHPvzA9Y"><span class="yt-uix-button-content">Undo</span></button>

          </div>
      </div>

    </div>

    <button type="button" class="yt-ui-menu-item yt-uix-menu-close-on-select  dismiss-menu-choice" data-feedback-token="AB9zfpIm-CiiRjci8V1eFnNgOh_aaLP6rRifvbQJ-N5dmWvA41mhvXZALDF59pHHD7-YXHb5OAWKDiPY6Pdw9o68wNOH_mpObt8hNUi5xIO0zTv1ROq9NLiFHT73UpEENbjLP1RMDRdH" data-action="replace-enclosing-action" data-innertube-clicktracking="CO8BEKk7IhMIgtfmp5r-yQIVVmFYCh1b2QYpKI4e">
    <span class="yt-ui-menu-item-label">Not interested</span>
  </button>


      </li>
  </ul>
</div></div>
  </div>
</div></div><div class="yt-lockup-notifications-container hid"></div></div></li>

li外面讨一个ul


youtube的行为
- 增加一点页面的大小，每个视频的图片大小是不变的；只是增加了两步的margin
