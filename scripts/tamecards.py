import os
import random
import sys

from modules import scripts, script_callbacks, shared

warned_about_files = {}
tamecard_dir = scripts.basedir()



class TamecardsScript(scripts.Script):
    def title(self):
        return "Simple tamecards"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def replace_tamecard(self, text, gen):
        if " " in text or len(text) == 0:
            return text

        replacement_file = os.path.join(tamecard_dir, "tamecards", f"{text}.txt")
        if os.path.exists(replacement_file):
            with open(replacement_file, encoding="utf8") as f:
                return f.read().splitlines()[gen]
        else:
            if replacement_file not in warned_about_files:
                print(f"File {replacement_file} not found for the ___{text}__ tamecard.", file=sys.stderr)
                warned_about_files[replacement_file] = 1

        return text

    def process(self, p):
        gen = 0
        original_prompt = p.all_prompts[0]

        for i in range(len(p.all_prompts)):

            prompt = p.all_prompts[i]
            prompt = "".join(self.replace_tamecard(chunk, gen) for chunk in prompt.split("___"))
            p.all_prompts[i] = prompt
            gen += 1

        if original_prompt != p.all_prompts[0]:
            p.extra_generation_params["Tamecard prompt"] = original_prompt


def on_ui_settings():
    shared.opts.add_option("tamecards_same_seed", shared.OptionInfo(False, "Use same seed for all images", section=("tamecards", "Tamecards")))


script_callbacks.on_ui_settings(on_ui_settings)
