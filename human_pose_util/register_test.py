import matplotlib.pyplot as plt
from human_pose_util.register import register_skeletons, register_datasets
from human_pose_util.register import get_dataset
from human_pose_util.register import get_skeleton
from dataset.normalize import normalized_view_data, normalized_p3w
from skeleton import vis3d

register_skeletons(h3m=True, eva=True, mpi_inf=True)
register_datasets(h3m=True, eva=True)
# register_converters(h3m_eva=True)
print('Registration successful!')

# dataset = dataset_register['h3m']

for dataset_id, target_skeleton_id in [['h3m', 's24'], ['eva', 's14']]:
    dataset = get_dataset(dataset_id)
    for mode in ['eval', 'train']:
        print('Getting normalized_view_data...')
        normalized_view_data(dataset, modes=mode)

        print('Getting normalized_p3w...')
        normalized_dataset, p3w = normalized_p3w(
            dataset, modes=mode, target_skeleton_id=target_skeleton_id)

skeleton = get_skeleton(normalized_dataset.attrs['skeleton_id'])
print(p3w.shape)
vis3d(skeleton, p3w[0])
plt.show()
