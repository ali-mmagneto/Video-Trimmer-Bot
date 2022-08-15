import time, os

from datetime import datetime as dt
from telethon import events
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata, bash
from ethon.pyutils import rename


from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3

@Client.on_message(filters.video)
async def trim(bot, message): 
    msg = await bot.send_message(chat_id, "`işlem yapılıyor..`")
    if message.video:
         file_name = message.video.file_name
    elif message.document:
         file_name = message.document.file_name
    elif message.audio:
         file_name = message.audio.file_name
    else:
         file_name = None

    if file_name is None:
        file_name = user_id
    DT = time.time()
    path = os.path.join(
            DOWNLOAD_DIR,
            user_id,
            random,
            file_name
        )
    filepath = await message.download(
        file_name=path,
        progress=progress_for_pyrogram,
        progress_args=("`İndiriliyor...`", msg, c_time))
    return await msg.edit(f"indirirken hata oluştu.\n\n@mmagneto'ya danış...") 
    try:
        await edit.edit("kesiliyor.")
        bash(f'ffmpeg -i {filepath} -ss {st} -to {et} -acodec copy -vcodec copy {out}')
        out2 = file_name + '_2_' + '.mp4'
        rename(out, out2)
    except Exception as e:
        print(e)
        return await msg.edit(f"Kesilirken bir hata oldu.\n\n@mmagneto'ya danış...", link_preview=False)
    UT = time.time()
    text = f"{out2}"
    try:
        metadata = video_metadata(out2)
        width = metadata["width"]
        height = metadata["height"]
        duration = metadata["duration"]
        attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
        video = await bot.send_video(
            out2,
            supports_streaming=True,
            caption=caption,
            thumb=thumb,
            duration=duration,
            width=width,
            height=height,
            progress=progress_for_pyrogram,
            progress_args=("`Yükleniyor...`", msg, c_time)
        )
        await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG3, attributes=attributes, force_document=False)
    except Exception:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            print(e)
            return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
      
