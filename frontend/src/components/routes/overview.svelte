<script>
  import { Link } from "svelte-routing";
  import { pageTransitionValue1, pageTransitionValue2 } from "../../stores";
  import { onMount } from "svelte";

  onMount(() => {
    $pageTransitionValue1 = 0;
    $pageTransitionValue2 = 0;
  });
</script>

<div>
  <button>
    <a href="auth/u/signup">Signup</a>
  </button>
  <button>
    <a href="auth/u/login">Login</a>
  </button>
</div>
