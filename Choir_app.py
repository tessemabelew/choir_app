# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Choir App", layout="wide")

menu = ["Landing", "Gallery", "Calendar", "Lyrics", "Files", "Announcements"]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Landing":
    st.title("🎶 Welcome to Our Choir Portal")
    st.image("winde1.jpg", width=600)
    st.markdown("""
    #### Quick Info
    - Choir practice every Thrusday at 7PM
    - Sunday Service: 9:00AM
    - Contact: tessemabelew@gmail.com
    """)

elif choice == "Gallery":
    st.title("📸 Choir Gallery")
    st.image("choir_atwondie.jpg", caption="At Wondie mels", use_column_width=True)

elif choice == "Calendar":
    st.title("🗓 Choir Calendar")
    st.markdown("""
    **Upcoming Events:**
    - **July 10**: Practice session
    - **August 10**: Community outreach performance
    - **July 20**: Sunday Choir Lead
    """)

elif choice == "Lyrics":
    st.title("🎵 Song Lyrics")
    songs = [
    {
        "title": "በረከትና ጥበብ ምስጋና",
        "lyrics": """
1.ከስሞች በላይ ታላቅ ስም ያለዉ ኢየሱስ ነው፣ 
እግዚአብሔር ያለልክ ከፍ ከፍ የረገዉ፣ 
ስሙ ድንቅ መካር ኃያል የሆነዉ ኢየሱስ ነው፣ 
በአብ ቀኝ በክብር የተቀመጠዉ፡፡ 

	በረከትና ጥበብ ምስጋና፣ 
	ለታረደው በግ ለኢየሱስ ምስጋና፣ 
	አሁንም /2/ ይድረሰዉ ምስጋና እንደገና፡፡

2.አለቆች ስልጣናት የሚገዙለት ኢየሱስ ነው፣ 
ቅዱሳን መላዕክት የሚሰግዱለት፣ 
አልፋና ኦሜጋ ኤልሻዳይ ቅዱስ ኢየሱስ ነው፣
የፍጥረታት ጌታ የነገስታት ንጉሥ፡፡ 
	
	በረከትና ጥበብ ምስጋና፣ 
	ለታረደው በግ ለኢየሱስ ምስጋና፣ 
	አሁንም /2/ ይድረሰዉ ምስጋና እንደገና፡፡

3.ፍቅሩ የማይለወጥ ምህረቱ የበዛ ኢየሱስ ነዉ፣ 
የዘለአለም ካህን በህይወት የሚኖረዉ፣ 
በደሙ አጥቦ ቀድሶ ያቆመን ኢየሱስ ነዉ፣ 
ዳግም የወለደን ለርስቱ የለየን፡፡ 
	
በረከትና ጥበብ ምስጋና፣ 
	ለታረደው በግ ለኢየሱስ ምስጋና፣ 
	አሁንም /2/ ይድረሰዉ ምስጋና እንደገና፡፡

AV : https://www.youtube.com/watch?v=xHgXstA8d0g
"""
    },
    {
        "title": "አሁንስ ጣፍጦኛል",
        "lyrics": """
1.መርከብ ያለ መሪ እንደሚዋዥቀው 
ነበረ ህይወቴ ማእበል የሞላው፣ 
ወደጌታ ኢየሱስ ከመጣሁ በኋላ 
ይህ አይቻለሁ ኑሮዬ ሲሞላ፡፡ /2/

አሁንስ ጣፍጦኛል /2/ 
ከጌታ ጋር መኖር እጅጉን ጥሞኛል፡፡

2.እንደ ማራ ውሃ ይመር የነበረው፣ 
ያ የጥንቱ ዘመን ኑሮዬ የቀድሞው፣ 
አሁን ግን በጌታ ሁሉም ተለውጦ 
ሌሎቹን ይጣራል መአዛ አግኝቶ /2/ 

አሁንስ ጣፍጦኛል /2/ 
ከጌታ ጋር መኖር እጅጉን ጥሞኛል፡፡


3.ጌታን በማወቄ ቢንቀኝ ብዙ ሰው፣ 
በእርሱ ያገኙትን እኔ ነኝ የማውቀው 
ስለዚህ ዝም በሉኝ ጌታዬን ላክብረው 
ለውዴ ውለታ እንዲያውም ሲያንሰው ነው፡፡ /2/

አሁንስ ጣፍጦኛል /2/ 
ከጌታ ጋር መኖር እጅጉን ጥሞኛል፡፡

4.በርሃቡም ዘመን ጠግቤ አድሬአለሁ፣
ማድጋዬ ሞልቶ ሲፈስ አይቻለሁ፣ 
በክፉውም ዘመን ሰላም አግኝቻለሁ፣ 
ታዲያ ይህን ጌታ እንዴት እተዋለሁ፡፡ /2/

አሁንስ ጣፍጦኛል /2/ 
ከጌታ ጋር መኖር እጅጉን ጥሞኛል፡፡

"""
    },
    {
        "title": "ሊነጋ ሲል ጨለማው ይበረታል!",
        "lyrics": """
ሊነጋ ሲል ጨለማው ይበረታል ከቶ የማይነጋ ይመስላል
ንጉስ እግዚአብሔር ይናገራል ጨለማውም ይታዘዘዋል
(ይታዘዘዋል ይታዘዘዋል ጨለማውም ይታዘዘዋል) 2X

1.እግዚአብሔር ከኛ ጋር ከሆነ ይህ ሁሉ ለምን ደረሰ
አባቶቻችን ያሉን ታምራት የት አለ ሲፈጸም በኛ ህይወት
ብሎ ገዴዎን ተስፋ ሲቆርጥ ለካስ ነበር ከሱ የሚበልጥ
የአብርሃም አምላክ ተገለጠ ጠላቶቹንም ተበቀለ

2.ኤልያስ ታላቅ የእግዚአብሔር ሰው እሳት ከሰማይ ያወረደው
በኤልዛቤል ዛቻ እሮጠ ክትክታ ዛፍ ስር ተቀመጠ
አሁንስ በቃኝ ነፍሴን ውሰድ ሲል እኔስ ከአባቶቼ አልበልጥ
የእግዚአብሔር መልአክም ዳሰሰው መንገድህ ሩቅ ነው ብላ አለው

3.ለኔም ዛሬ ጨለማው ቢበረታ ቢመስለኝ እንኳ የማይነጋ
በመጠበቂያዬ ላይ እቆማለሁ መልሴ ሲመጣ አየዋለሁ
የተናገረኝ ቢዘገይም እጠብቃለሁ ተስፋ አልቆርጥም
የአባቶቼ አምላክ ይገለጣል ብቻውን ተአምር ያደርጋል

4.ድንኳን የሚሆን መኖርያዬ ቢያስቸግረኝም ይህ ስጋዬ
እንቁዬን በእርያ ፊት አልጥልም ወደቀድሞው አልመለስም
ይህ ሞላ ይህ ጎደለ እያለ ውዴ ኢየሱሴንም ሊያስጥለኝ
ቢሞክር ዛሬም አላገኘኝ የአባቶቼ አምላክ ስላለልኝ

AV: https://www.youtube.com/watch?v=Vids9w73NmM
"""
    },
    {
        "title": "ማዳን የአንተ ነው!",
        "lyrics": """
ማዳን የአንተ ነው ሁሉ ተችሎሃል 
ስምህም ብርቱ ነው በሰልፍ አሸንፏል 
እኔ ምስክር ነኝ በዘመኔ ሁሉ
ለታመኑት ሁሉ ሰርቷል እንደ ቃሉ (2 *)

1.የዮርዳኖስ ውሃ እጅግ ሞልቶ ነበር
ካህናት ሲገቡ ሆኗል እንዳልነበር
ከእያሱ ጋር ያለ ዛሬም ከእኛ ጋር ነው
የነ ሙሴ አምላክ ማዳን አይሳነው

2.ቀንደ መለከቱን ሲነፉ ካህናት
ድምጻቸውን አንስተው ሲጮሁ ባንድነት
የኢያሪኮ ግንቡ ተንዶ ፈራርሷል
ይሄ ታላቅ ክንዱ አሁንም ይሰራል

3.በሶስት መቶ ሰዎች ጠላትን የመታ 
የጌደኦን አምላክ ክንዱ የበረታ 
ጸንቼ ቆማለሁ ማዳን የእርሱ ነው
የእስራኤል አምላክ ዛሬም ኤልሻዳይ ነው

4.ሳምሶን በደሊላ ተፈትኖ ሲወድቅ 
ፍልስጤማውያን ቢዘባበቱበት 
እባክህ አስበኝ ብሎ ተማጸነው 
ጠላቱን መታለት የበቀል አምላክ ነው


"""
    },
    {
        "title": "በዋጋ ገዝቶኛል !",
        "lyrics": """
በዋጋ ገዝቶኛል የራሴ አይደለሁም 
የመንፈሱ ማደሪያ ለእርሱ የተለየሁኝ (2*)

1.ልጁን ልኮ የታደገኝ ከጨለማ ያስመለጠኝ
ወደ ብርሃን ወደ እራሱ የጠራኝ ነኝ ለመንግስቱ
ከእንግዲህማ ላልኖር ለእኔ ለስጋዬ ለፈቃዴ
የለየኝ ነኝ ለእራሱ የመረጠኝ ለእርስቱ 

2.በሚሞተው በስጋዬ እንዳነግሰው በዘመኔ
ይህን ወዶ ለይቶኛል እንዳመልከው አድርጎኛል
ከቶ አይደለም የመረጠኝ በጥበቤ በእዉቀቴ
ሊገልጥ ወዶ ምህረቱን ሰው ያረገኝ መድሃንቴ

3.በክርስቶስ በመሆኔ ሆኛለሁ አዲስ ፍጥረት 
አሮጌውን አስወግዶ አጠበኝ በቅዱስ ደም
መቅደሱና የመንፈሱ ማደሪያ አርጎ አድሮብኛል
ከእንግዲህማ ማንስ ሌላ ጌታ ይገዛኛል

4.ዝም እንዳልል ያየሁትን በሕይወቴ በኑሮዬ
ከእሳት ነጥቄ እንዳወጣ ሌሎችን ደግሞ ታድጌ
አንባሳደር አድርጎኛል የመንግስቱ ልዩ ዜጋ
እሰራለሁ ቀን ሌት ሳልል ተልኮዬን ሳልዘነጋ
"""
    }
]
# Create a title list for the dropdown
    song_titles = [song["title"] for song in songs]
    selected_title = st.selectbox("Select a song", song_titles)

    # Find selected song and display lyrics
    selected_song = next(song for song in songs if song["title"] == selected_title)
    st.text_area("Lyrics", selected_song["lyrics"], height=300)

elif choice == "Files":
    st.title("📂 Choir Files")
    st.markdown("Download important choir documents:")
    st.download_button("Download Choir bylaw", "Bylaw content here", file_name="IEECChoirbylaw.docx")
    st.download_button("Download song mater", "song master content here", file_name="Songs_master.pdf")

elif choice == "Announcements":
    st.title("📢 Announcements")
    announcements = [
        "🎤 Solo practice this Friday at 5PM.",
        "🚌 Transport arrangements for the outreach event are finalized.",
        "🎉 Choir celebration dinner on July 21st after service."
    ]
    for note in announcements:
        st.success(note)


