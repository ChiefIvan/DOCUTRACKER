<script>
  // @ts-nocheck

  import { backendAddress } from "../stores";

  import Form from "./entries/form.svelte";
  import Input from "./entries/input.svelte";

  let email = "";
  let password = "";
  let cnfrmPassword = "";
  let api = `${backendAddress}reset`;

  const handleReset = (e) => {
    email = e.detail;
  };
</script>

<Form {email} {api} on:resetInput={handleReset}>
  <Input
    inputName={"Email"}
    inputType={"email"}
    inputAutocomplete={"on"}
    inputValue={email}
    on:input={(e) => (email = e.target.value)}
  />
  <button>Reset Password</button>
</Form>
