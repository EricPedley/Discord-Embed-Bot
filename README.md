# Discord bot that saves you from epic embed fails
![Epic embed clutch gif](https://i.giphy.com/media/l3sSaz59d5fy0tdew9/giphy.webp)

## The problem: 
discord doesn't embed instagram or tiktok links
## The solution: 
bot that automatically webscrapes the link for the video url, then makes a request for the video, save as bytes, then uploads to discord as file attachment 

### current WIP status:
the embed for instagram should work, except right now in testing I'm getting 429 errors so I can't say for sure it works. Tiktok videos are more complicated because it won't let you just http request the video link; that gives you a 401 forbidden error. I looked at how the browser makes the request and it seems like it sends an initial request, then sends a second request that includes extra headers that allow it to get the video.
