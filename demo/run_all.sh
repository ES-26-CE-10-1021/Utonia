#!/usr/bin/env bash
# Run all demos that don't require external inputs, writing .ply files to demo/exports/.
# Run from the repo root:  bash demo/run_all.sh
# Extra flags (e.g. --wo_color, --wo_normal) are forwarded to every demo.

DEMOS=(
  0_pca_indoor
  1_similarity
  2_sem_seg
  3_batch_forward
  4_pca_hk
  5_pca_manipulation
  6_pca_object
  7_pca_outdoor
)

failed=()
for name in "${DEMOS[@]}"; do
  echo
  echo "=== demo/${name}.py ==="
  if ! PYTHONPATH=./ python "demo/${name}.py" "$@"; then
    echo "!! demo/${name}.py FAILED"
    failed+=("${name}")
  fi
done

echo
echo "Done. Outputs written to demo/exports/"
echo "Note: demo/8_pca_video.py requires --input_video; run it separately."

if [ ${#failed[@]} -ne 0 ]; then
  echo
  echo "Failed demos: ${failed[*]}"
  exit 1
fi
