<script>
  import { winEvent, expand, dark, openProfile } from "../../stores";
  let scrolled;

  $: {
    scrolled > 50 ? ($winEvent = true) : ($winEvent = false);
    $dark
      ? (document.body.className = "body-dark")
      : (document.body.className = "body-light");
  }

  const close = () => {
    if ($expand) {
      $expand = false;
    }
  };

  const closeProfile = (e) => {
    if ($openProfile && e.target.closest(".profiles") === null) {
      $openProfile = false;
    }
  };
</script>

<svelte:window
  bind:scrollY={scrolled}
  on:scroll={() => {
    close();
  }}
  on:resize={() => {
    close();
    closeProfile();
  }}
  on:click={(e) => {
    close();
    closeProfile(e);
  }}
/>
