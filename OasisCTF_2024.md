# It all starts with a flag
It all started with challenge that asked me to add the flag it has given. So began my first ever CTF.
Ready PLayer?
.
.
.
.
*Goooooo*
<br><br><br>

## I am Optimus Prime
As you set out to warn the OASIS community about the Trojan's infiltration, your efforts are abruptly interrupted. Mechanoids, armed and dangerous, have been dispatched by IOI to stop you. These mechanical enforcers close in, their metallic limbs glinting in the digital light. It's time to fight back and escape their relentless assault. Can you outmaneuver these foes and stay alive? https://blogpost.oasis.cryptonite.live

This was the prompt, on going to the said link I reach the website that looked something like this

![Blogpost challenge](/Photo%20one.png)

Since it is one of those webpage challenge my first instint was to go into inspect element and search for if I can find any functionality to the save button??? Did't find anything

So i went to that discord and the hin that was given said something about `"robot-only" no no zone`.
On chatgpting It turns out in webpages there are some areas that are restricted for most people. To keep web crawlers away from this areas, developers add sections telling which area is prohibited.

Following on that I add `/robots.txt` to the url and got into a page giving this output
    User-agent: *
    Disallow: /hiddenFlag

Meaning the /hiddenFlag area is prohibited for everyone, so that means I will need tp try somnething in the console to get the flag output.

So I searched how do we usually get access to this kind of area????? 

It tells me to use different https methods to test the effects but there are so many https method? which one do I use??? 
To check this I use `curl -X OPTIONS -i https://blogpost.oasis.cryptonite.live`
and get this
    HTTP/2 400
    cache-control: public, max-age=0, must-revalidate
    content-type: text/html; charset=utf-8
    date: Thu, 10 Oct 2024 18:00:58 GMT
    server: Vercel
    strict-transport-security: max-age=63072000
    x-vercel-cache: MISS
    x-vercel-id: bom1::iad1::cntpm-1728583258673-75fa10664b80
    content-length: 13

    Invalid token

The token is missing, so to find I take a wild guess and find it in cookies and found something very interetsing
`user_token:"f308d3f1-7f1a-4e8d-a370-6347ea545322"`

Using this I use the options method again
Now all i need is to check GET and HEAD methods
    
