<script>
  import { fetchData, backendAddress } from "../../stores";
  import { onMount } from "svelte";

  import Auth from "../entries/auth.svelte";

  const homeAddress = `${backendAddress}index`;
  const homeErrMsg = "";

  let userId = "";
  let authBind;

  onMount(() => {
    document.title = "DOCUTRACKER | Home";
    userId = localStorage.getItem("remembered") || "";
    authBind.getEndPoint(homeAddress, homeErrMsg, {
      Authorization: `Bearer ${userId}`,
    });
  });
</script>

<Auth bind:this={authBind} />
<section>
  <!-- {#if Object.keys($fetchData).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$fetchData["email"]}</h2>
    <p>ID: {$fetchData["id"]}, Username: {$fetchData["user_name"]}</p>
  {/if} -->

  Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi alias labore
  sint sunt magni assumenda iure. Omnis perspiciatis expedita repellendus sint
  ipsum harum porro deserunt unde odit beatae nesciunt eveniet, nam, autem ut,
  nihil obcaecati illo esse excepturi praesentium mollitia ipsa consequuntur
  assumenda commodi. Quod reiciendis assumenda minus sequi maiores quidem
  corrupti obcaecati vero, ex culpa voluptas exercitationem minima deserunt
  eveniet consequatur ut, molestiae optio similique officia dolores dignissimos.
  Aspernatur quo error provident voluptatum ipsa ea. In minus ut perspiciatis,
  blanditiis optio, dolore sed inventore sapiente neque atque itaque,
  consectetur officiis repellendus facere ratione. Laboriosam sed mollitia sunt
  natus eveniet, animi sint ducimus amet magni assumenda facilis, totam rem nam
  tenetur obcaecati non atque ex dolorem placeat tempora! Consequuntur doloribus
  veniam delectus repellendus, quis vitae amet eos fugit tempora! Repellendus
  voluptatibus maiores commodi voluptas dolore earum cumque facere unde quas!
  Tempora reiciendis quidem excepturi quae incidunt quibusdam molestias
  molestiae! Ipsam impedit sapiente voluptatum illo laboriosam. Nostrum fuga
  voluptas enim nam officiis sit iusto similique harum excepturi magnam dolor,
  consequuntur, impedit, odit voluptate mollitia quasi? Numquam quo sit tempore,
  at placeat doloribus temporibus officiis error animi qui id ex, corrupti odit,
  aut eum dignissimos hic accusamus quisquam ut consequatur dolorum. Aliquid
  doloribus voluptatibus, voluptatem illum, ipsam ipsa quam nam repudiandae
  exercitationem deleniti sed reprehenderit ex illo. Culpa molestiae accusantium
  laborum placeat repudiandae commodi dolor, quaerat dicta aut deserunt.
  Expedita ea, dicta nihil non incidunt aspernatur pariatur earum magnam dolores
  dolore animi eligendi quasi amet saepe delectus a odio, quaerat laudantium
  enim cumque illum voluptatem, reiciendis labore! Itaque doloremque illum
  quasi. Veniam autem delectus, officiis quisquam odio voluptate quidem eveniet,
  animi doloribus quam recusandae excepturi distinctio quibusdam maiores illum
  nemo accusamus itaque fuga quo laboriosam! Corrupti, quibusdam deleniti! Ut
  nam, illo nulla magni incidunt dolores omnis fugiat iure impedit iste error,
  expedita iusto! Ea nisi obcaecati similique laborum, vel, voluptates quod
  eaque voluptas nemo repudiandae deleniti qui, ab perferendis id repellendus
  beatae minus sunt. Excepturi esse voluptatem praesentium. Cupiditate mollitia
  assumenda officia, asperiores deleniti tenetur expedita incidunt eum accusamus
  quia tempore. Laboriosam repellendus, quos incidunt magni ipsa aliquid,
  ducimus debitis atque iste ratione, beatae a aliquam! Cum, placeat soluta
  debitis velit itaque a, aut, rem iure error porro magnam est nobis libero.
  Sequi deleniti, recusandae molestias repudiandae corporis quia quidem hic.
  Ullam minus eius dicta vero nesciunt. Doloremque porro eius enim, odio quam
  pariatur molestiae at eum odit numquam nesciunt culpa labore! Rem laborum
  architecto voluptas aut tempore possimus reprehenderit, iure ad explicabo
  alias nemo voluptatum inventore praesentium vero debitis numquam provident
  doloribus laudantium porro, quibusdam dolores nihil. Perferendis cumque
  recusandae ad neque omnis perspiciatis aperiam dolorum ipsum, labore quis hic
  facilis corrupti itaque blanditiis amet! Harum maxime vitae consequatur eaque.
  Quis porro architecto nostrum repellat ratione at culpa debitis facere magnam
  aperiam a illo hic similique rem, veniam alias sit ut velit est! Error, dolor
  repellendus. Quidem mollitia fugit asperiores reprehenderit aliquam totam
  autem, accusamus, eveniet doloribus quam quaerat voluptatibus molestiae iure
  voluptatem similique voluptate magnam ad aut. Quidem nobis enim rem sunt
  eveniet nihil doloremque excepturi reprehenderit, quaerat magni doloribus unde
  exercitationem? Quos voluptatum quas sapiente. Blanditiis expedita iure
  doloribus nemo? Blanditiis esse, ipsum numquam eligendi quod debitis
  voluptatum molestias accusamus velit iusto itaque magni perspiciatis! Quam
  fugiat animi molestiae tempora possimus obcaecati, ipsa ducimus nemo. Quidem
  neque unde vitae harum nam perspiciatis? Alias facere quia ducimus iste vero
  architecto laudantium debitis. Eum laborum qui tenetur cupiditate repellendus
  voluptatem, dolores est deserunt accusamus. Quibusdam magnam totam odio beatae
  nostrum eos itaque non at tenetur nobis numquam praesentium eligendi quo, qui
  sed dolor ea molestiae iste unde quam impedit optio, quia harum. Provident
  alias eveniet dignissimos modi temporibus fuga nesciunt repudiandae nihil
  quasi! Illum impedit pariatur quisquam deserunt quam ipsa, sequi quas alias
  inventore eius exercitationem eligendi, earum magni ullam harum,
  necessitatibus ipsum similique facere sed hic. Harum, sunt reiciendis dolor
  ducimus impedit dignissimos assumenda sapiente nulla similique itaque
  architecto maxime sed facilis debitis. Ipsa perspiciatis dolor deleniti.
  Quaerat voluptatem nesciunt dolorem quibusdam, harum similique! Debitis
  architecto rerum autem quas inventore culpa tempora ab, dignissimos eaque
  optio, nemo nam veniam assumenda labore voluptates voluptatem eius illum
  voluptas ratione nesciunt asperiores quidem molestias impedit itaque? Optio
  aperiam nesciunt assumenda dignissimos obcaecati magni cumque alias atque
  accusamus cupiditate, saepe placeat ullam aspernatur expedita quia amet eaque
  et dolore! Iure dolorum vitae maiores iusto voluptates quis? Sunt facere aut
  reiciendis unde dolore excepturi dicta quia nisi, molestiae ducimus atque
  dolorum ullam, voluptates doloribus enim qui, voluptate pariatur fuga
  reprehenderit non temporibus. Voluptatibus, nam officiis! Excepturi eligendi
  pariatur numquam eveniet? Mollitia doloribus inventore numquam magnam quos
  ipsa laboriosam fugit natus nemo iste, odio similique molestias nam, quae,
  animi officia? Nihil, vero doloremque. Iure excepturi cupiditate ratione odit
  perferendis harum voluptatem molestiae? Quae at culpa incidunt, cum enim,
  natus quis minus vel odit minima amet cupiditate sapiente! Dolorum molestiae
  cum voluptatibus molestias accusantium voluptates enim ipsa natus, odit neque
  maxime a. Porro, odit. Reprehenderit voluptatem vitae facilis? Nisi natus,
  iste illum quidem modi eum earum fugiat quas ab repellat molestias,
  consequatur necessitatibus dolorem enim vero dicta! Provident sapiente
  accusantium, numquam dolore iure animi voluptas, voluptate excepturi
  voluptatum ipsa eaque sed tempore commodi dignissimos? Facilis sequi in ea rem
  totam, quo quisquam quam voluptatum numquam cumque officia consequuntur
  repellat sit sed aut deleniti dignissimos est deserunt dolorem rerum
  cupiditate ipsam culpa! Odio temporibus esse, iste vero incidunt architecto.
  Aperiam corrupti pariatur blanditiis quo molestiae, eius dolore fuga ipsum!
  Eius nobis blanditiis enim perspiciatis non, obcaecati, quasi tenetur ab iure
  nostrum alias recusandae commodi ex debitis laudantium earum et officia
  doloremque possimus quibusdam! Assumenda molestias atque quaerat sint quidem
  natus quia voluptas aut nemo deleniti nulla placeat nisi ex laboriosam
  recusandae voluptatem possimus incidunt, nihil ipsam vel. Cum dolorem odio
  pariatur reiciendis dicta non quia. Dolores nostrum, quae fugiat adipisci
  tempore ipsa velit beatae qui architecto non dignissimos aspernatur sequi
  minima mollitia. Maxime voluptatem qui, nam iste officia beatae officiis
  vitae, temporibus exercitationem odio inventore velit esse repellat ipsam
  delectus, necessitatibus minima nihil vero consequatur quibusdam est neque?
  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Suscipit velit
  fugiat neque nulla molestiae perferendis beatae dolore aut porro perspiciatis
  alias, laudantium hic animi, impedit dignissimos iusto. Architecto ab sapiente
  iste voluptate cum! Illum omnis nihil deserunt voluptatem debitis eum,
  doloremque deleniti, cumque nemo aspernatur ea vero consequuntur. Iste
  obcaecati necessitatibus accusantium! Ea, sapiente at. Odio laudantium porro
  cumque similique, provident vero incidunt veniam corporis sit dolores vel
  autem, necessitatibus quasi molestiae repudiandae modi dolorum, ex laborum
  aperiam saepe expedita dolore tempore. Placeat, corrupti! Excepturi, rerum
  laudantium assumenda illo est eaque nihil quod eligendi. Error sed quaerat
  nulla praesentium sapiente? Temporibus vero consequatur dolor quisquam. Eum
  officiis doloribus cum recusandae in? Dolor eos laboriosam illo sapiente cum
  consequuntur perferendis quia provident ut molestiae officia eum excepturi
  facere, omnis deleniti placeat expedita eius. Consectetur magnam vitae optio
  quibusdam voluptatum quis modi nihil, rerum nam, neque architecto omnis itaque
  nobis assumenda aliquid ad provident deserunt non dicta odit excepturi! Atque
  deleniti praesentium unde. Recusandae et dolore amet voluptate sit dolor,
  harum odio vitae ipsam omnis iusto cupiditate ratione esse totam maiores,
  aliquam ullam corrupti. Nostrum eveniet inventore iusto. Temporibus id officia
  quidem, cupiditate pariatur facilis perspiciatis similique aperiam doloremque
  blanditiis cumque aspernatur magni unde sed, obcaecati fuga saepe non sapiente
  tenetur incidunt eius odit quam earum consectetur. Alias repudiandae cumque
  amet tempora ea maiores sequi cum veritatis qui, inventore iure quam soluta
  quia facilis asperiores excepturi quis molestias vero dicta, sit ad eos illo
  accusantium accusamus! Vitae, voluptatibus ut libero inventore fugiat
  consectetur dolor provident? Culpa alias deleniti reprehenderit ad ex ab, quae
  in. Modi sit mollitia perferendis beatae velit id odit placeat qui labore
  eveniet quidem fugit similique, neque iure ipsum omnis ratione quibusdam
  veniam eos, et ea nulla? Odio laboriosam error vel quod repudiandae officia
  aliquam rem! Nesciunt earum similique accusamus. Sint repudiandae, maxime
  eveniet incidunt possimus accusantium doloremque impedit soluta minus odio,
  asperiores voluptatibus, earum nostrum eos. Labore nobis temporibus blanditiis
  adipisci accusamus quis repellat numquam veritatis nihil excepturi quibusdam,
  fuga tempore, iure neque pariatur fugit assumenda eum autem voluptas,
  voluptate voluptates dolores dicta. Inventore repellat veniam est ad facere,
  sit accusamus nisi beatae alias vitae commodi quo assumenda dicta consectetur
  praesentium numquam et soluta exercitationem quae cum! Distinctio quod
  inventore nulla voluptates ipsam aspernatur ea suscipit mollitia, est laborum
  ex doloremque illum cumque quia assumenda vitae placeat. Architecto accusamus
  at velit cumque, ullam soluta! Quod labore totam sequi illo, quis dolores
  accusantium ea iure amet pariatur repudiandae quos alias, exercitationem rerum
  distinctio laudantium perspiciatis quam odio incidunt vel? Odio amet sequi
  voluptatem iste error repellat voluptatum, debitis alias iusto eum
  perspiciatis! Est porro quis aut hic harum dolorum quos sint autem
  reprehenderit dolore libero quas, deserunt officiis, repellat voluptas atque?
  Corporis minima placeat necessitatibus quidem aliquid nihil et. Repellat
  expedita aliquam perspiciatis rerum mollitia ut voluptate molestias illo ad!
  Maxime aspernatur inventore laboriosam autem molestias, illo repellat quaerat
  vitae itaque quam hic voluptates possimus quidem dignissimos suscipit qui unde
  recusandae soluta eveniet aperiam. Eligendi, rem? Perspiciatis temporibus ut
  quo quasi inventore expedita doloremque nesciunt magni eos et non, voluptate,
  labore debitis laudantium nobis soluta tenetur tempore unde. Suscipit quis
  voluptas ad sed laboriosam laborum fuga nemo sunt pariatur, autem, aliquid
  vero magni facilis rem minima exercitationem reprehenderit ullam similique
  tenetur veritatis veniam dolorem! Asperiores, placeat sint repudiandae beatae
  ea accusamus odit aperiam quod temporibus quidem nihil quo fugiat debitis unde
  doloremque odio voluptatem veniam, reiciendis quas aliquid! Mollitia, a cumque
  tenetur sint earum dolor vero facere accusamus dolorem consectetur sunt,
  libero placeat, obcaecati exercitationem minus commodi? Numquam ipsa corrupti
  aliquid voluptates recusandae, soluta impedit repellendus ab deleniti, nostrum
  explicabo fugiat molestiae officia sit amet tempora dolorum, earum optio
  tenetur! Laudantium quam repellendus minima doloribus voluptates velit
  pariatur aut, quae nobis dignissimos dolor! Fugit exercitationem provident
  eius quae pariatur cupiditate maxime, assumenda commodi a, sint molestiae,
  tempora et modi nostrum ducimus natus numquam fuga eum iste impedit inventore?
  Culpa rem ipsam aliquam nesciunt earum aspernatur dolorum magni sapiente, vel,
  eligendi libero repellat ullam? Necessitatibus, officiis nisi ea corrupti
  exercitationem ut a odio doloremque aspernatur laborum id porro distinctio
  eius aliquam? Quia aliquid a at maxime natus tempore omnis ex distinctio
  numquam suscipit, eum porro facere officiis ab magni deleniti amet. Nam in
  ipsum minima inventore numquam voluptatem maxime adipisci, illo iste quod
  harum nobis quasi non labore nihil laboriosam fugit eos neque natus
  voluptates, facilis consequatur? Harum tempore sapiente nesciunt soluta, rerum
  excepturi aspernatur nisi quod laudantium quisquam ducimus non, modi est
  quidem perferendis eveniet. Veritatis facere quod dolores doloribus reiciendis
  laborum quam a magnam consectetur qui consequatur eveniet nam dolorum, quae,
  ad incidunt explicabo hic, odio eligendi quasi rem. Reiciendis praesentium
  doloribus odio architecto quaerat consectetur incidunt, saepe quos sit quod
  similique magni quam laudantium id qui a rem aperiam! Nihil unde pariatur
  numquam quis quasi eius libero officia, odit maiores omnis, suscipit
  dignissimos cum, soluta voluptate sit? Aspernatur, eaque laboriosam. Ipsam
  dolorum ullam voluptatibus maxime maiores tenetur minus aliquid animi quaerat
  quas iure eos rerum eveniet, possimus accusantium obcaecati voluptates commodi
  quod quo, error perferendis. Officiis, quos et laudantium ducimus autem
  mollitia ipsa repellendus qui esse, voluptates natus saepe minus animi nihil
  dolor, corporis sint cumque magnam nobis! Exercitationem illo commodi nihil
  suscipit. Dolorum maxime ut vel fuga? Deleniti, temporibus magnam!
  Necessitatibus et officia, ullam recusandae magni, error enim ut
  reprehenderit, laudantium quidem architecto soluta voluptate perferendis at
  ducimus. Velit, cum nulla. Assumenda aliquam quidem quas et possimus incidunt
  repellendus doloribus voluptatem! Dolorum explicabo praesentium quo, facere
  ut, fugit culpa officia ad atque labore obcaecati, rem illo voluptatibus hic
  ratione placeat ipsa adipisci amet velit esse. Impedit eos accusantium magnam
  delectus qui et iure reiciendis vero id? Distinctio, maiores! Cupiditate
  itaque laborum, voluptates quae amet libero incidunt! Vel hic explicabo
  commodi voluptate repudiandae voluptates nulla, ipsum rerum cupiditate esse
  excepturi eligendi veniam? Praesentium laudantium asperiores assumenda
  mollitia perspiciatis, fugit pariatur nesciunt, qui voluptatibus labore vel
  hic culpa dolorem nulla odit iste sunt eaque! Temporibus, atque est quibusdam
  animi quos minus unde, facere blanditiis velit dolorem odio veritatis.
</section>

<style>
  /* div {
    display: flex;
    justify-content: center;
    align-items: center;
  } */
  section {
    flex: 2;
  }
</style>
