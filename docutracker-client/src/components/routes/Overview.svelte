<script lang="ts">
  import { navigate } from "svelte-routing";

  import Button from "../shared/Button.svelte";

  const handleNavigate = (path: string) => {
    navigate(path);
  };
</script>

<main>
  <h1>This is Overview</h1>
  <Button on:click={() => handleNavigate("/auth/login")}>Login</Button>
  <Button on:click={() => handleNavigate("/auth/signup")}>Signup</Button>
</main>
