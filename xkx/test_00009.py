from dotenv import load_dotenv  # 用于加载环境变量
from langchain.globals import set_debug, set_verbose

set_debug(True)
set_verbose(True)
load_dotenv()  # 加载 .env 文件中的环境变量


from langserve import RemoteRunnable

# dependency the lang serve, run  test_008.py


# text from here : https://lore.kernel.org/all/9aa26719-0614-4b83-b638-ac48b69be4e5@apevzner.com/#t

strength = """

My name is Alexander Pevzner, and I live in Russia, Moscow.

I'm probably one of these "Russian trolls", mentioned by Linus in his 
message a couple of days ago.

Regardless of that, I use Linux as my primary OS since 1.2.13 kernel (so 
about 30 years for now) and I've contributed few lines of code (or, most 
likely, few thousand of lines of code) to make driverless printing and 
scanning work on Linux, so if you use one of those modern multifuction 
printers, this is very likely that among other stuff you use one of 
couple of my projects already on our personal computer.

As for me, the free software movement is the important thing. Really 
important. It makes people to cooperate. Not only individuals, but 
people from competing corporations. The free software movement sometimes 
"glues" people stronger, that money interest, which often works to 
separate people.

The whole history of the humanity can be seen as a history of ugly wars 
(the war is always ugly regardless of its reasons, because it always 
kills the human in a person).

 From another side, the whole history of the humanity can be seem as a 
history of cooperation. It was cooperation that allowed us to get out of 
the caves into outer space, to create computers and to write operating 
systems and other software for them.

Any war will some day end and any government will some day become part 
of the history, but the story of human cooperation has a chance to 
outlive the history.

In that sense, free software works in direction just opposite to the 
war. It lets people to cooperate, to see humans in another person's eyes 
(and code). Even when we are separated by the war.

And it puts a lot of responsibility to the free software leaders, 
because they not only manage lines of code, but somehow define edges of 
the future of the entire humanity. At least, in some aspects.

As a professional, I'm trying to cleanly separate software development 
from any kind of politics (probably, the same we all expect from the 
medical doctors). When I receive PR for review or a bug report, I look 
only to proposed code changes or bug description, regardless on who send 
me it.

The Linux Foundation is the community of software professionals. I 
understand that this is US organization and it is sometimes obliged by 
the US laws and regulation.

What would I expect from the professional organization in a case like 
this. The following:
1. The clear public note, that according to some US regulation the 
people from the sanctioned organizations cannot longer act as kernel 
maintainers
2. The personal communication with each of them, with explanation what 
is going on and verification that these persons are under sanctions
3. The clear public note, now with the list of affected persons, 
explaining that they will be removed from the maintainers list and with 
the great thanks for the work that they have done before.
4. Inclusion of these peoples into the kernel's hall of fame (the 
CREDITS list)

Nothing of this has be done, unfortunately. This is very, very pity :(

--
With the best regards, Alexander Pevzner (pzz@apevzner.com)"})
    """

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
remote_chain.invoke({"language": "Chinese", "text": strength})
