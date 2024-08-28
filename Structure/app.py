from flask import Flask, render_template, request

app = Flask(__name__)

recommendations = {
    "Arts and creativity": {
        "Writing": "Compile an Illustrated Storybook or Poetry Collection: Write a series of short stories or poems and create accompanying illustrations or artwork. Publish the collection as an e-book, physical book, or online series.",
        "Reading": "Curate an Online Art and Literature Review: Start a blog or digital magazine where you review and analyze literature through the lens of visual arts. Discuss how certain books inspire or relate to different artistic movements or styles.",
        "Coding": "Develop an Art Gallery Website: Create a personal or community website that functions as a virtual art gallery. Users can upload and showcase their artwork, and the site could feature interactive elements like virtual tours or art critiques.",
        "Exercising": "Design a Fitness & Art Fusion Workshop: Combine physical exercise with creativity by designing a workshop where participants engage in art activities like painting or sculpting after a workout, exploring how physical movement influences creativity.",
        "Painting": "Create a Series of Thematic Paintings: Focus on a particular theme (e.g., mental health, nature, or abstract concepts) and create a series of paintings around it. Host an exhibition or share them on social media or a personal website.",
        "Photography/videography": "Launch a Visual Storytelling Project: Combine photography and videography to tell a story through visual media. This could be a photo essay, a short film, or a series of video interviews with artists, documenting their creative processes.",
        "Learning/personal development": "Start a Creative Skills Challenge: Dedicate time to learning a new artistic skill (e.g., digital painting, sculpture, or graphic design) and document your progress. Share tutorials, challenges, and your creations online.",
        "Volunteering and community work": "Organize a Community Mural Project: Lead a project to create a public mural in your community. Engage local artists and volunteers, and involve the community in the design and painting process."
    },
    "Music": {
        "Writing": "Write and Record an Original Album or EP: Compose original songs, write lyrics, and record your own music. Release the album or EP on platforms like Spotify, Bandcamp, or SoundCloud.",
        "Reading": "Create a Music Analysis Blog: Start a blog where you analyze lyrics, compositions, and music theory in your favorite songs or genres. Offer insights into how music and literature intertwine.",
        "Coding": "Develop a Music Composition App: Build an app that helps users create their own music. It could include features like a digital piano, beat maker, or songwriting prompts.",
        "Exercising": "Design a Music-Driven Workout Playlist: Curate and share workout playlists with different tempos and rhythms to match various exercise routines. You could also create a series of workout videos synchronized to music.",
        "Painting": "Create Album Art for Musicians: Offer your artistic skills to create custom album covers or promotional materials for local musicians or your own music projects.",
        "Photography/videography": "Document a Local Music Scene: Use photography or videography to capture live performances, interviews with musicians, and behind-the-scenes moments. Create a documentary or a photo series that tells the story of the local music community.",
        "Learning/personal development": "Learn and Document a New Instrument: Pick up a new instrument and document your learning journey through videos, blog posts, or a podcast. Share tips and tutorials as you progress.",
        "Volunteering and community work": "Organize a Charity Concert: Plan and host a charity concert featuring local artists. Use your skills in music, event planning, and community organizing to raise funds for a cause you care about."
    },
    "Sports": {
        "Writing": "Start a Sports Blog or Magazine: Write about your favorite sports, athletes, training tips, and game strategies. You could also cover local sports events and profiles of athletes in your community.",
        "Reading": "Create a Sports Book Review Blog: Review and discuss books on sports, fitness, and athlete biographies. Offer insights on how these readings can inspire and motivate others in their own sports journeys.",
        "Coding": "Develop a Sports Tracking App: Build an app that helps athletes track their training progress, set goals, and analyze their performance. You could include features like a workout log, performance metrics, and motivational challenges.",
        "Exercising": "Design a Personal or Community Fitness Program: Create a structured fitness program tailored to a specific sport or fitness goal. Share the program through a blog, social media, or by organizing group workouts in your community.",
        "Painting": "Create Sports-Themed Art: Combine your love for sports and art by creating paintings or drawings of athletes, iconic sports moments, or abstract interpretations of movement and energy in sports.",
        "Photography/videography": "Document a Sports Season: Capture the highs and lows of a sports season through photography or videography. Focus on a local team, and create a documentary or photo series that tells the story of their journey.",
        "Learning/personal development": "Learn and Teach a New Sport: Take up a new sport and document your learning process. Share tutorials, tips, and your experiences through videos or blog posts, encouraging others to try the sport as well.",
        "Volunteering and community work": "Organize a Community Sports Day: Plan a sports day event in your community, encouraging participation from people of all ages and skill levels. This could include a variety of sports and activities, fostering community spirit and physical fitness."
    },
    "Performance and expression": {
        "Writing": "Write and Perform an Original Play or Monologue: Write a script for a play or a series of monologues and perform them live or record them for online sharing. You could involve other actors or do a solo performance.",
        "Reading": "Host a Theatrical Book Club: Start a book club focused on plays, screenplays, and books about acting or theater. Host discussions and, if possible, perform scenes or readings with the group.",
        "Coding": "Create a Digital Storytelling Platform: Develop an interactive platform where users can create and share their own stories or performances. The platform could allow for multimedia integration, combining text, audio, and video.",
        "Exercising": "Design a Movement-Based Performance: Choreograph a performance that combines physical exercise with expressive movement, such as a dance routine or a physical theater piece. Share it through a live performance or recorded video.",
        "Painting": "Create Visual Backdrops for Performances: Use your painting skills to design and create visual backdrops or set pieces for theatrical performances, concerts, or dance shows.",
        "Photography/videography": "Film and Edit a Short Performance Film: Produce a short film that focuses on performance art, dance, or a theatrical piece. Use your videography skills to capture and edit the performance in a way that enhances the storytelling.",
        "Learning/personal development": "Master and Document a New Acting Technique: Study a specific acting technique or performance method (e.g., Meisner, Method Acting) and document your learning process. Share insights, exercises, and your progress through blog posts or videos.",
        "Volunteering and community work": "Organize a Community Talent Show: Plan and host a talent show in your community, providing a platform for people of all ages to express themselves through performance. Use the event to raise awareness or funds for a cause."
    },
    "Science and technology": {
        "Writing": "Write and Publish a Science Blog or eBook: Share your knowledge and insights on scientific topics, research, or technological advancements.",
        "Reading": "Create a Science Book Review Channel: Review and discuss books on scientific topics, discoveries, and biographies of scientists.",
        "Coding": "Develop an Educational Tech Tool or App: Build an app or tool that helps people learn about science or technology.",
        "Exercising": "Design a Tech-Enhanced Fitness Program: Create a fitness program that leverages technology, such as wearable fitness trackers, apps, or virtual reality workouts.",
        "Painting": "Create Science-Inspired Art: Combine your interest in science and art by creating paintings or digital art that explores scientific concepts.",
        "Photography/videography": "Document a Science Experiment Series: Use photography or videography to capture and explain a series of science experiments.",
        "Learning/personal development": "Learn and Build a New Tech Skill: Dedicate time to learning a new technology or programming language.",
        "Volunteering and community work": "Organize a Community Science Fair: Plan a science fair in your community, encouraging people of all ages to participate."
    },
    "Nature and environment": {
        "Writing": "Start an Environmental Blog or Podcast: Write about environmental issues, sustainability tips, or nature conservation.",
        "Reading": "Create a Nature Book Club: Start a book club focused on nature, environmental issues, and sustainability.",
        "Coding": "Develop a Conservation App: Create an app that helps users track their environmental impact or find ways to reduce waste.",
        "Exercising": "Plan a Nature-Focused Fitness Routine: Design a fitness program that involves outdoor activities like hiking, cycling, or running.",
        "Painting": "Create Eco-Friendly Art: Use sustainable materials to create art that raises awareness about environmental issues.",
        "Photography/videography": "Document Environmental Issues: Use your photography or videography skills to capture environmental challenges.",
        "Learning/personal development": "Learn and Practice Sustainable Living: Dedicate time to learning about sustainable practices.",
        "Volunteering and community work": "Organize a Community Clean-Up or Tree-Planting Event: Lead a project focused on environmental conservation."
    },
    "Entrepreneurship and business": {
        "Writing": "Write a Business Blog or eBook: Share your insights, tips, and experiences in entrepreneurship or business management.",
        "Reading": "Create a Business Book Review Blog: Review and discuss books on entrepreneurship, business strategies, and biographies.",
        "Coding": "Develop a Business Tool or App: Build a digital tool or app that helps small businesses or entrepreneurs.",
        "Exercising": "Plan a Business-Focused Fitness Challenge: Create a fitness program that promotes wellness among entrepreneurs and business professionals.",
        "Painting": "Design Branding Materials for Small Businesses: Offer your artistic skills to create logos, business cards, or promotional materials.",
        "Photography/videography": "Document Entrepreneurial Journeys: Use photography or videography to capture the stories of entrepreneurs and business owners.",
        "Learning/personal development": "Learn and Apply a New Business Skill: Focus on developing a specific business skill, such as marketing, finance, or management.",
        "Volunteering and community work": "Organize a Business Mentorship Program: Create a program that connects aspiring entrepreneurs with experienced mentors."
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation', methods=['POST'])
def recommendation():
    passion = request.form.get('passion')
    activity = request.form.get('activity')
    recommendation = recommendations.get(passion, {}).get(activity, "No recommendation available for the selected options.")
    return render_template('index.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
