
import aiohttp, asyncio, mimetypes, os, re
from userge import userge, Message


####################################################################################

async def get_server(s):
    async with s.get('https://www.zippyshare.com') as r:
      r.raise_for_status()
      match = re.search(r'var server = \'(www\d{1,3})\';', await r.text())
      if not match:
          raise None
      return match.group(1)


def check_size(path):
    total = os.path.getsize(path)
    if total > 524288000:
        raise False
    return True


def get_mime_type(fname):
    mime_type = mimetypes.guess_type(fname)[0]
    if mime_type == None:
        mime_type = "application/octet-stream"
    return mime_type

def extract(html):
    regex = (r'onclick=\"this.select\(\);" value="(https://www\d{1,3}'
             r'.zippyshare.com/v/[a-zA-Z\d]{8}/file.html)')
    url = re.search(regex, html)
    if not url:
        return None
    return url.group(1)


async def upload(s, path, private = False):
    if not (server := await get_server(s)):
        return "<i>Failed to find zippy server...</i>"
    if not check_size(path):
        return "<i>File shouldn't exceeds 500MB...</i>"
    fname = os.path.basename(path)
    url = "https://{}.zippyshare.com/upload".format(server)
    data = aiohttp.FormData({
        'name': fname,
        'private' if private else 'notprivate': "true"
    })
    data.add_field('file', open(path, 'rb'),
        filename = fname,
        content_type = get_mime_type(fname)
    )
    async with s.post(url, data=data) as r:
        r.raise_for_status()
        return extract(await r.text())

####################################################################################

@userge.on_cmd("zipup", about={
  "header": "Zippyshare Uploader",
  "description": "Upload a file to zippyshare",
  "flags": {"-p": "To make it private"},
  "usage": "{tr}zipup [file path or reply to file's message]"
}, del_pre=True)
async def _zipup(msg: Message):
  await msg.edit("<i>Processing...</i>")
  _input = msg.filtered_input_str
  replied = msg.reply_to_message
  if not _input and not replied:
      return await msg.edit("<i>Either reply to file or input path of it..</i>")
  path = _input or await replied.download()
  if not os.path.isfile(path):
      return await msg.edit("<i>Provided path doesn't exist...</i>")
  async with aiohttp.ClientSession() as s:
      res = await upload(s, path, ("p" in msg.flags))
  await msg.edit(f"<b>Response from Server...</b>\n\n<code>{res}</code>")