<script lang="ts">
  import { adminUser } from "../../store";
  import { navigate } from "svelte-routing";

  import Button from "../shared/Button.svelte";
  import Input from "../shared/Input.svelte";
  import Header from "../lib/Header.svelte";
  import Footer from "../lib/Footer.svelte";

  let inputBind = false;
  let admin = "";
  let formBind: HTMLFormElement;

  const handleSubmit = () => {
    $adminUser = admin;
    inputBind = false;
    formBind.reset();
    (document.activeElement as HTMLElement).blur();
    navigate("/admin");
  };
</script>

<main>
  <form bind:this={formBind} on:submit|preventDefault={handleSubmit}>
    <Input
      inputType="text"
      inputName="Admin Username"
      on:input={(e) => (admin = e?.target.value)}
      bind:focusedInput={inputBind}
    />
    <Button>Login</Button>
  </form>
</main>
