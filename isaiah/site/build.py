# Builds the preview site pages from shared header/footer.
# Run: python3 build.py
import os
HERE = os.path.dirname(os.path.abspath(__file__))

AMAZON = "https://www.amazon.com/dp/1456848488"
EMAIL = "kenrad1977@gmail.com"

NAV = [("book.html", "The Book"), ("programs.html", "Programs"), ("if-your-brother-sins.html", "If Your Brother Sins"),
       ("about.html", "About"), ("podcast.html", "Podcast"), ("contact.html", "Contact")]

def head(title, desc, current):
    cur = ' aria-current="page"'
    links = "\n".join(
        f'        <a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap">
<link rel="stylesheet" href="site.css">
</head>
<body>
<div class="preview-bar">Preview of a proposed new design for theisaiahproject.name. Buttons and forms are for review only.</div>
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="index.html"><img src="img/p-mark.png" alt="" width="30" height="29"><span>The Isaiah Project</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
{links}
        <a class="btn btn-gold" href="book.html#buy">Get the book</a>
    </nav>
  </div>
</header>
<main>
'''

FOOT = f'''</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand">The Isaiah Project, Inc.</div>
        <p>Let our healing begin. The Isaiah Project is a 501(c)(3) nonprofit founded by Deacon Kenneth L. Radcliffe in Harlem, New York.</p>
        <div class="btn-row"><a class="btn btn-gold" href="contact.html#donate">Donate</a></div>
      </div>
      <div>
        <h4>Explore</h4>
        <a href="book.html">The Book</a>
        <a href="programs.html">The Recovery Room</a>
        <a href="if-your-brother-sins.html">If Your Brother Sins&hellip;</a>
        <a href="podcast.html">Podcast</a>
      </div>
      <div>
        <h4>Get in touch</h4>
        <a href="contact.html">Contact Deacon Ken</a>
        <a href="contact.html#speaking">Invite him to speak</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
    <div class="foot-base">&copy; 2026 The Isaiah Project, Inc. &middot; The Recovery Room uses the Twelve Steps and Twelve Traditions with written permission from AA World Services, Inc.</div>
  </div>
</footer>
<script>
(function () {{
  var b = document.querySelector(".menu-btn"), n = document.getElementById("nav");
  if (b) b.addEventListener("click", function () {{ var o = n.classList.toggle("open"); b.setAttribute("aria-expanded", o); }});
  function toast(msg) {{
    var t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); t.textContent = msg;
    document.body.appendChild(t); setTimeout(function () {{ t.remove(); }}, 3600);
  }}
  document.querySelectorAll("[data-preview]").forEach(function (el) {{
    el.addEventListener("click", function (e) {{ e.preventDefault(); toast(el.getAttribute("data-preview")); }});
  }});
  document.querySelectorAll("form[data-preview-form]").forEach(function (f) {{
    f.addEventListener("submit", function (e) {{ e.preventDefault(); toast(f.getAttribute("data-preview-form")); }});
  }});
}})();
</script>
</body>
</html>
'''

PRAISE = '''<div class="wrap"><div class="praise">
  <blockquote><p>&ldquo;A Good Read.&rdquo;</p><cite><b>Timothy Michael Cardinal Dolan</b>Archbishop of New York</cite></blockquote>
  <blockquote><p>&ldquo;Others have attempted to write about our nation&rsquo;s addiction to racism, but this book sets the standard.&rdquo;</p><cite><b>Sandy Bernabei, LCSW</b>Liberation Psychotherapist</cite></blockquote>
  <blockquote><p>&ldquo;At a time when racism is a public health crisis, this book is a vital tool for healing.&rdquo;</p><cite><b>Barbara C. Wallace, PhD</b>Teachers College, Columbia University</cite></blockquote>
</div></div>'''

SIGNUP = '''<section><div class="wrap"><div class="signup">
  <div>
    <p class="eyebrow" style="color:var(--ink)">Free guide</p>
    <h2>The 12 Steps of Racism Recovery</h2>
    <p class="lede">A two-page guide from Deacon Ken that walks through each Step as it applies to healing from racism. Free, sent straight to your inbox.</p>
  </div>
  <form class="form" data-preview-form="Preview: this will send the free guide once the email service is connected.">
    <label for="g-name">First name</label><input id="g-name" name="name" autocomplete="given-name">
    <label for="g-email">Email</label><input id="g-email" name="email" type="email" autocomplete="email" required>
    <button class="btn btn-dark" type="submit">Send me the free guide</button>
    <p class="note">One short email a month. Unsubscribe anytime.</p>
  </form>
</div></div></section>'''

pages = {}

pages["index.html"] = head("The Isaiah Project | Racism Is a Disease. It Can Be Treated.",
  "Deacon Kenneth L. Radcliffe applies the 12 Steps of Alcoholics Anonymous to the disease of racism. Get the book, join the Recovery Room, and let our healing begin.", "index.html") + f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Let our healing begin</p>
      <h1>Racism is a disease. <em>It can be treated.</em></h1>
      <p class="lede">For over 30 years in recovery work, Deacon Kenneth L. Radcliffe has seen what racism does to people. His book applies the 12 Steps of Alcoholics Anonymous to healing from it.</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="book.html#buy">Get the book</a>
        <a class="btn btn-line" href="#guide">Free: The 12 Steps guide</a>
      </div>
    </div>
    <img class="cover" src="img/book-cover.jpg" alt="Cover of Applying Alcoholics Anonymous Principles to the Disease of Racism by Kenneth L. Radcliffe" width="351" height="529">
  </div>
</section>
{PRAISE}
<section>
  <div class="wrap">
    <div class="sec-head">
      <p class="eyebrow">The idea</p>
      <h2>What if we treated racism the way we treat addiction?</h2>
    </div>
    <div class="truths">
      <div class="truth"><div class="k">First</div><h3>It is a disease</h3><p>Like alcohol and drug dependence, racism is a mental illness that damages the lives it touches: Black men, women and children, other people of color, and many others.</p></div>
      <div class="truth"><div class="k">Second</div><h3>It can be arrested</h3><p>It cannot be cured, and it cannot be controlled. But like any addiction, it can be stopped. &ldquo;It can be arrested, pun intended.&rdquo;</p></div>
      <div class="truth"><div class="k">Third</div><h3>It can be treated</h3><p>The Twelve Steps, Twelve Traditions, slogans and Serenity Prayer of AA give people harmed by racism a proven path to recovery.</p></div>
    </div>
  </div>
</section>
<section class="night">
  <div class="wrap">
    <p class="pull">&ldquo;Show me a man or woman who has not achieved their dreams, and I will show you a man or woman whose life has been affected by mental illness, addiction to alcohol, drugs, substance misuse, racism and violence.&rdquo;</p>
    <p class="pull-by"><b>Deacon Ken Radcliffe</b>, Founder, The Isaiah Project</p>
  </div>
</section>
<section>
  <div class="wrap author">
    <div class="photo-slot">Photo of Deacon Ken goes here</div>
    <div>
      <p class="eyebrow">Meet the author</p>
      <h2>Deacon Kenneth L. Radcliffe</h2>
      <p class="lede">Known across Central Harlem as Deacon Ken, he has spent his life walking with people through addiction, incarceration and the wounds of racism.</p>
      <ul class="creds">
        <li>Permanent Deacon in the Archdiocese of New York for 47 years, serving St. Charles Borromeo, Resurrection &amp; All Saints in Harlem</li>
        <li>20 years as Administrative Chaplain for the NYC Department of Correction, including Rikers Island and &ldquo;The Tombs&rdquo;</li>
        <li>Certified Alcohol and Substance Abuse Counselor (CASAC) and Recovery Coach trainer certified by NYS OASAS</li>
        <li>Creator of the award-winning Dream Makers reentry program</li>
      </ul>
      <div class="btn-row"><a class="btn btn-dark" href="about.html">Read his story</a></div>
    </div>
  </div>
</section>
<section class="stone">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Get involved</p><h2>Ways to begin healing</h2></div>
    <div class="cards">
      <div class="card"><span class="tag">Free</span><h3>The Recovery Room</h3><p>A safe space for people whose lives have been affected by racism, using the 12 Steps with written permission from AA World Services since 2016.</p><a class="more" href="programs.html#recovery-room">How it works</a></div>
      <div class="card"><span class="tag">For groups</span><h3>Parish &amp; Group Study</h3><p>Bring the book to your parish, ministry, book club or recovery program with group pricing and a guide for leading the discussion.</p><a class="more" href="book.html#groups">Group options</a></div>
      <div class="card"><span class="tag">Speaking</span><h3>Invite Deacon Ken</h3><p>Talks and workshops for churches, schools, conferences and reentry programs, including &ldquo;Let Our Healing Begin.&rdquo;</p><a class="more" href="contact.html#speaking">Request a talk</a></div>
      <div class="card"><span class="tag">Reentry</span><h3>Dream Makers &amp; St. Dismas</h3><p>Programs for men and women on probation or parole, and training for faith communities who visit the incarcerated.</p><a class="more" href="programs.html#dream-makers">Learn more</a></div>
    </div>
  </div>
</section>
<section>
  <div class="wrap split">
    <img src="img/if-your-brother-sins.jpg" alt="Poster for If Your Brother Sins, a Catholic visual commentary on race and racism" width="900" height="1200" loading="lazy">
    <div>
      <p class="eyebrow">Presentation</p>
      <h2>&ldquo;If Your Brother Sins&hellip;&rdquo;</h2>
      <p class="lede">A Catholic visual commentary on race and racism, calling the Church to discernment on restitution, reparations and restorative justice.</p>
      <p>The printed report was taken to Rome by Cardinal Dolan and presented to the Dicastery for Promoting Integral Human Development at the Vatican.</p>
      <div class="btn-row"><a class="btn btn-dark" href="if-your-brother-sins.html">About the presentation</a></div>
    </div>
  </div>
</section>
<div id="guide"></div>
{SIGNUP}
''' + FOOT

pages["book.html"] = head("The Book | Applying Alcoholics Anonymous Principles to the Disease of Racism",
  "Buy Deacon Kenneth L. Radcliffe's book as an e-book or paperback, or order copies for your parish or group.", "book.html") + f'''
<section>
  <div class="wrap book-top">
    <img class="cover" src="img/book-cover.jpg" alt="Book cover" width="351" height="529">
    <div>
      <p class="eyebrow">The book</p>
      <h1 style="font-size:clamp(32px,4.6vw,48px)">Applying Alcoholics Anonymous Principles to the Disease of Racism</h1>
      <div class="meta-row"><span>Kenneth L. Radcliffe</span><span>58 pages</span><span>Xlibris</span></div>
      <p class="lede">Racism is a disease, a mental illness, with symptoms much like alcoholism. It can&rsquo;t be cured, but it can be treated. This short, direct book shows how.</p>
      <div class="buy" id="buy">
        <div class="opt main"><span class="fmt">E-book</span><span class="price">$3.99</span><span class="desc">Instant download. Read on any phone, tablet or computer.</span><a class="btn btn-gold" href="#" data-preview="Preview: this will open secure checkout once PayPal or Stripe is connected.">Buy the e-book</a></div>
        <div class="opt"><span class="fmt">Paperback</span><span class="price">$15.99</span><span class="desc">Printed copy shipped to your door from Amazon.</span><a class="btn btn-dark" href="{AMAZON}" target="_blank" rel="noopener">Buy on Amazon</a></div>
        <div class="opt wide" id="groups"><span class="fmt">For parishes, ministries &amp; programs</span><span class="price" style="font-size:26px">Group study orders</span><span class="desc">Ten or more copies at a group price, with a discussion guide for leading the book over 12 weeks.</span><a class="btn btn-line" href="contact.html#groups">Request group pricing</a></div>
      </div>
    </div>
  </div>
</section>
<section class="stone">
  <div class="wrap narrow">
    <p class="eyebrow">What&rsquo;s inside</p>
    <h2>A new way to understand racism</h2>
    <ul class="list-check">
      <li>Why racism behaves like a disease, and why it can be treated even though it cannot be cured</li>
      <li>How racism creates dysfunction in the lives of African Americans and other people of color</li>
      <li>How the principles of Alcoholics Anonymous apply to recovery from racism</li>
      <li>The role of the Black Church in resisting racism in America</li>
    </ul>
    <p style="color:var(--muted);font-size:15px">Draft summary for Deacon Ken to review and rewrite in his own words.</p>
  </div>
</section>
<section><div class="wrap narrow"><p class="eyebrow">What readers say</p><h2>Praise for the book</h2></div></section>
{PRAISE}
<section>
  <div class="wrap narrow faq">
    <p class="eyebrow">Questions</p>
    <h2>Before you buy</h2>
    <details><summary>Do I need the book to join the Recovery Room?</summary><p>Yes. Reading the book is required before joining the Recovery Room, so everyone in the group starts from the same foundation.</p></details>
    <details><summary>How do I get the e-book after I pay?</summary><p>You&rsquo;ll get a download link right away on screen and by email.</p></details>
    <details><summary>Can my church or program order copies?</summary><p>Yes. Group orders of ten or more come with group pricing and a discussion guide. <a href="contact.html#groups">Ask about group orders</a>.</p></details>
    <details><summary>Who is this book for?</summary><p>Anyone whose life has been affected by racism, and the pastors, counselors, recovery coaches and social workers who walk with them.</p></details>
  </div>
</section>
{SIGNUP}
''' + FOOT

pages["programs.html"] = head("Programs | The Isaiah Project",
  "The Recovery Room, Let Our Healing Begin, The Dream Makers, and the St. Dismas Re-entry Project.", "programs.html") + '''
<div class="page-head"><div class="wrap"><p class="eyebrow">Programs</p><h1>Four ways the Isaiah Project helps people heal</h1><p class="lede">From a 12-Step group for people harmed by racism to reentry programs for people coming home from prison.</p></div></div>
<section><div class="wrap">
  <div class="prog" id="recovery-room">
    <div class="when">Free &middot; By appointment &middot; In person or on Zoom</div>
    <h2>The Recovery Room</h2>
    <p>The Recovery Room is a safe space for victims of racism, in particular Black men, women and children, &ldquo;JUST US,&rdquo; whose lives have been affected by racism and racist behavior for over 400 years since being brought to the Americas in chains. It also welcomes other people of color and ethnicities whose lives have been affected by racism.</p>
    <p>It uses the Twelve Steps, Twelve Traditions, slogans and Serenity Prayer of Alcoholics Anonymous, with written permission from AA World Services, Inc. since August 2016.</p>
    <div class="callout"><p><b>To join:</b> read <a href="book.html">the book</a> first, then <a href="contact.html">contact Deacon Ken</a> to schedule your first meeting. Meetings are free.</p></div>
  </div>
  <div class="prog" id="healing">
    <div class="when">A community conversation</div>
    <h2>Let Our Healing Begin!</h2>
    <p>A conversation on mental illness, alcohol and drug dependence, and substance misuse. The disease of chemical dependence as a behavioral health and brain disorder is discussed, along with the question at the heart of the Isaiah Project: is racism a mental disorder, and what is its impact on our community? Includes readings from Deacon Ken&rsquo;s book and invited speakers.</p>
    <div class="btn-row"><a class="btn btn-dark" href="contact.html#speaking">Bring this to your community</a></div>
  </div>
  <div class="prog" id="dream-makers">
    <div class="when">Reentry &middot; For people on parole or probation</div>
    <h2>The Dream Makers</h2>
    <p>An award-winning reentry program brought to the New York State Department of Correction and Community Supervision for fourteen years. Its mission is to reduce recidivism and increase the chance of employment for men and women on probation or parole, by helping them see that changes in behavior, attitude and values can break the cycle of substance misuse, anger, racism and violence.</p>
  </div>
  <div class="prog" id="st-dismas">
    <div class="when">Training for faith communities</div>
    <h2>St. Dismas Re-entry Project</h2>
    <p>A &ldquo;how to&rdquo; pastoral ministry workshop for faith communities who want to visit incarcerated men, women and children, offering spiritual comfort through prayer, song and hope. St. Dismas, the thief who repented on the cross beside Jesus, is proof that it is never too late. &ldquo;&hellip;in prison and you visited me.&rdquo; Matthew 25:36</p>
    <div class="btn-row"><a class="btn btn-dark" href="contact.html">Schedule a workshop</a></div>
  </div>
</div></section>
''' + SIGNUP + FOOT

pages["if-your-brother-sins.html"] = head("If Your Brother Sins | The Isaiah Project",
  "A Catholic visual commentary on race and racism by Deacon Kenneth L. Radcliffe.", "if-your-brother-sins.html") + '''
<div class="page-head"><div class="wrap"><p class="eyebrow">Presentation</p><h1>&ldquo;If Your Brother Sins&hellip;&rdquo;</h1><p class="lede">A Catholic visual commentary on race and racism.</p></div></div>
<section><div class="wrap split">
  <div>
    <p>&ldquo;If Your Brother Sins&hellip;&rdquo; is a sight-and-sound presentation by Deacon Ken Radcliffe on the Atlantic slave trade and slavery as the major source of free labor and capital building, and a call for Church discernment on restitution, reparations and restorative justice, beginning with the Roman Catholic Church.</p>
    <p>The printed report was taken to Rome by Timothy Cardinal Dolan, who presented it to Cardinal Michael Czerny, S.J., Prefect of the Dicastery for Promoting Integral Human Development, who referred it to the Regional Coordinator for North America for review and study.</p>
    <p>It is essential viewing for Catholic parishes, ministries and organizations working for social justice and struggling to understand the disease of racism.</p>
    <div class="callout"><p><b>Viewings on Zoom</b> are available by appointment when five or more people are interested.</p></div>
    <div class="btn-row"><a class="btn btn-dark" href="contact.html">Request a viewing</a></div>
  </div>
  <img src="img/if-your-brother-sins.jpg" alt="Poster for If Your Brother Sins" width="900" height="1200">
</div></section>
''' + FOOT

pages["about.html"] = head("About Deacon Kenneth L. Radcliffe | The Isaiah Project",
  "Deacon, former Rikers Island chaplain, addiction counselor and author Kenneth L. Radcliffe.", "about.html") + '''
<div class="page-head"><div class="wrap"><p class="eyebrow">About</p><h1>Rev. Kenneth L. Radcliffe, Deacon, Servant</h1><p class="lede">Founder of The Isaiah Project, Inc. and the Criminal &ldquo;JUST US&rdquo; Committee.</p></div></div>
<section><div class="wrap author">
  <div class="photo-slot">Photo of Deacon Ken goes here</div>
  <div class="narrow">
    <p>Deacon Ken Radcliffe, as he is affectionately known in the Central Harlem community, has served as a Permanent Deacon in the Archdiocese of New York for 47 years. He is assigned to the parish of St. Charles Borromeo, Resurrection &amp; All Saints in Harlem.</p>
    <p>He retired from the New York City Department of Correction as an Administrative Chaplain after 20 years of service, with assignments at Rikers Island, detention centers in the Bronx and Brooklyn, and the Manhattan Detention Complex, known as &ldquo;The Tombs.&rdquo; Since retiring, he designed the award-winning Dream Makers program, which he has brought to the New York State Department of Correction and Community Supervision for fourteen years.</p>
    <p>He began training as an alcoholism and chemical dependency counselor in 1993 and in 2018 completed training as a Certified Alcohol and Substance Abuse Counselor (CASAC). He is a trained Recovery Coach and is certified by New York State OASAS to train Recovery Coaches. He has worked as a relapse prevention specialist, co-occurring counselor and case manager, and has volunteered at St. Mother Teresa&rsquo;s Missionaries of Charity homeless shelter in the Bronx.</p>
    <h3 style="margin-top:36px">Writing</h3>
    <ul class="list-check">
      <li><a href="book.html"><i>Applying Alcoholics Anonymous Principles to the Disease of Racism</i></a></li>
      <li><i>The Crisis of the Poor in Black Urban America: A Challenge for the Roman Catholic Church</i></li>
      <li><i>The Crisis of the Poor in Black Urban America: The Challenge for a President and Corporate America</i></li>
      <li><a href="if-your-brother-sins.html">&ldquo;If Your Brother Sins&hellip;&rdquo;</a>, a Catholic visual commentary on race and racism</li>
    </ul>
    <div class="btn-row"><a class="btn btn-dark" href="contact.html#speaking">Invite Deacon Ken to speak</a></div>
  </div>
</div></section>
''' + PRAISE + FOOT

pages["podcast.html"] = head("Podcast | The Isaiah Project",
  "A Conversation on Race and Racism with Deacon Kenneth L. Radcliffe.", "podcast.html") + '''
<div class="page-head"><div class="wrap"><p class="eyebrow">Listen</p><h1>A Conversation on Race &amp; Racism</h1><p class="lede">Deacon Ken Radcliffe on the disease of racism, as a guest on the &ldquo;Alma, Am I Racist?&rdquo; podcast.</p></div></div>
<section><div class="wrap narrow">
  <div class="ep"><div class="num">01</div><div><h3>The Disease of Racism, Part 1</h3><p>With Lisa Smith, host of &ldquo;Alma, Am I Racist? An Anti-Racist, Pro-Black Podcast.&rdquo;</p></div><a class="btn btn-dark" href="https://almaamiracist.com/the-disease-of-racism-part-1/" target="_blank" rel="noopener">Listen</a></div>
  <div class="ep"><div class="num">02</div><div><h3>The Disease of Racism, Part 2</h3><p>The conversation continues on recovery, the 12 Steps and the Black Church.</p></div><a class="btn btn-dark" href="https://almaamiracist.com/the-disease-of-racism-part-2/" target="_blank" rel="noopener">Listen</a></div>
  <div class="callout"><p><b>Host a podcast?</b> Deacon Ken is available for interviews on faith, recovery, reentry and racial healing. <a href="contact.html#speaking">Invite him on your show</a>.</p></div>
</div></section>
''' + SIGNUP + FOOT

pages["contact.html"] = head("Contact | The Isaiah Project",
  "Contact Deacon Kenneth L. Radcliffe about the Recovery Room, speaking, group orders or donations.", "contact.html") + f'''
<div class="page-head"><div class="wrap"><p class="eyebrow">Contact</p><h1>Get in touch with Deacon Ken</h1><p class="lede">Questions about the Recovery Room, speaking invitations, group orders, or supporting the work.</p></div></div>
<section><div class="wrap contact-grid">
  <form class="form" data-preview-form="Preview: messages will go to Deacon Ken's email once the form service is connected.">
    <label for="c-name">Your name</label><input id="c-name" name="name" autocomplete="name" required>
    <label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required>
    <label for="c-phone">Phone (optional)</label><input id="c-phone" name="phone" type="tel" autocomplete="tel">
    <label for="c-topic">What is this about?</label>
    <select id="c-topic" name="topic"><option>Joining the Recovery Room</option><option>Inviting Deacon Ken to speak</option><option>Group or parish book order</option><option>If Your Brother Sins viewing</option><option>Donating</option><option>Something else</option></select>
    <label for="c-msg">Message</label><textarea id="c-msg" name="message"></textarea>
    <button class="btn btn-dark" type="submit">Send message</button>
  </form>
  <div class="info">
    <div><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <div id="speaking"><h3>Speaking &amp; workshops</h3><p>Deacon Ken speaks to parishes, schools, recovery conferences and reentry programs. Popular talks include &ldquo;Let Our Healing Begin&rdquo; and &ldquo;Is Racism a Mental Disorder?&rdquo;</p></div>
    <div id="groups"><h3>Group &amp; parish orders</h3><p>Ten or more copies of the book at a group price, with a 12-week discussion guide.</p></div>
    <div id="donate"><h3>Support the work</h3><p>The Isaiah Project, Inc. is a 501(c)(3) nonprofit. Gifts keep the Recovery Room free for everyone who needs it.</p><div class="btn-row" style="margin-top:12px"><a class="btn btn-gold" href="#" data-preview="Preview: this will open a secure donation page once connected.">Donate</a></div></div>
  </div>
</div></section>
''' + FOOT

for name, html in pages.items():
    with open(os.path.join(HERE, name), "w") as f:
        f.write(html)
print("built", len(pages), "pages")
